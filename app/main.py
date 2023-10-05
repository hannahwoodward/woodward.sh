from frontmatter import Frontmatter
from pathlib import Path
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import markdown
import re

templates = Jinja2Templates(directory='templates')

# ----- HELPERS -----
def get_entry_data(path, slug, raw=False):
    file = Frontmatter.read_file('data/' + path + '.md')
    entry = {
        'content': file['body'] if raw else markdown.markdown(file['body']),
        'metadata': file['attributes'],
        'slug': slug,
        'title': file['attributes']['title']
    }

    return entry

def get_entry_listings(path):
    posts = []
    for p in Path(f'data/{path}').glob('*.md'):
        slug = re.sub(rf'data/{path}/(.+)\.md', r'\g<1>', str(p))
        post = get_entry_data(f'{path}/{slug}', slug)
        if post and post['metadata']['enabled']:
            posts.append(post)

    return posts

# ----- PAGES -----
async def index(request):
    template_vars = {
        'request': request,
        'entry': {
            'title': 'About'
        }
    }

    return templates.TemplateResponse('index.jinja', template_vars)

# async def archive(request):
#     posts = []
#     for p in Path('data/archive').glob('*.md'):
#         slug = re.sub(r'data/archive/(.+)\.md', r'\g<1>', str(p))
#         post = get_entry_data('archive/' + slug, slug)
#         if post and post['metadata']['enabled']:
#             posts.append(post)
#
#     template_vars = {
#         'request': request,
#         'entry': {
#             'posts': posts,
#             'title': 'Archive'
#         }
#     }
#
#     return templates.TemplateResponse('archive.jinja', template_vars)
#
# async def archive_entry(request):
#     slug = request.path_params['slug']
#
#     template_vars = {
#         'request': request,
#         'entry': get_entry_data('archive/' + slug, slug)
#     }
#
#     return templates.TemplateResponse('_entry.jinja', template_vars)

def entry(path, template='_entry.jinja', raw=False):
    async def handle(request):
        slug = request.path_params['slug']

        template_vars = {
            'request': request,
            'entry': get_entry_data(path.format(slug=slug), slug, raw)
        }

        return templates.TemplateResponse(template, template_vars)

    return handle

def page(slug, template):
    async def handle(request):
        template_vars = {
            'request': request,
            'entry': get_entry_data(slug, slug)
        }

        return templates.TemplateResponse(template, template_vars)

    return handle


def page_listings(path, title, template):
    async def handle(request):
        posts = get_entry_listings(path=path)

        # Sort by newest post date
        posts = sorted(posts, key=lambda item: item['metadata']['post_date'])[::-1]

        template_vars = {
            'request': request,
            'entry': {
                'posts': posts,
                'title': title
            }
        }

        return templates.TemplateResponse(template, template_vars)

    return handle


def page_error(title):
    async def handle(request, exc):
        template_vars = {
            'request': request,
            'entry': {
                'title': title
            }
        }

        return templates.TemplateResponse('_error.jinja', template_vars, status_code=exc.status_code)

    return handle

exception_handlers = {
    404: page_error('404 - Not Found'),
    500: page_error('500 - Server Error')
}

middleware = [
    Middleware(GZipMiddleware, minimum_size=1000)
]

routes = [
    Route('/', endpoint=index),
    # Route('/archive', endpoint=archive),
    # Route('/archive/{slug}', endpoint=archive_entry),
    Route('/food', endpoint=page('food', '_entry.jinja'), name='food'),
    Route('/libs', endpoint=page('libs', 'libs.jinja'), name='libs'),
    Route('/pottery', endpoint=page_listings('pottery', 'Pottery', 'pottery.jinja'), name='pottery'),
    # Route('/slides', endpoint=page_listings('slides', 'Presentation slides', 'slides.jinja'), name='slides'),
    Route('/slides/{slug}', endpoint=entry('slides/{slug}', '_entry-slides.jinja', raw=True), name='slides_entry'),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, exception_handlers=exception_handlers, middleware=middleware, routes=routes)
