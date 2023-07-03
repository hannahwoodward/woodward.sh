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

def get_entry_data(path, slug):
    file = Frontmatter.read_file('data/' + path + '.md')
    entry = {
        'content': markdown.markdown(file['body']),
        'metadata': file['attributes'],
        'slug': slug,
        'title': file['attributes']['title']
    }

    return entry

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

async def food(request):
    slug = 'food'

    template_vars = {
        'request': request,
        'entry': get_entry_data(slug, slug)
    }

    return templates.TemplateResponse('_entry.jinja', template_vars)

async def libs(request):
    slug = 'libs'

    template_vars = {
        'request': request,
        'entry': get_entry_data(slug, slug)
    }

    return templates.TemplateResponse('libs.jinja', template_vars)

async def pottery(request):
    posts = []
    for p in Path('data/pottery').glob('*.md'):
        slug = re.sub(r'data/pottery/(.+)\.md', r'\g<1>', str(p))
        post = get_entry_data('pottery/' + slug, slug)
        if post and post['metadata']['enabled']:
            posts.append(post)

    # Sort by newest post date
    posts = sorted(posts, key=lambda item: item['metadata']['post_date'])[::-1]

    template_vars = {
        'request': request,
        'entry': {
            'posts': posts,
            'title': 'Pottery'
        }
    }

    return templates.TemplateResponse('pottery.jinja', template_vars)

def error_page(title):
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
    404: error_page('404 - Not Found'),
    500: error_page('500 - Server Error')
}

middleware = [
    Middleware(GZipMiddleware, minimum_size=1000)
]

routes = [
    Route('/', endpoint=index),
    # Route('/archive', endpoint=archive),
    # Route('/archive/{slug}', endpoint=archive_entry),
    Route('/food', endpoint=food),
    Route('/libs', endpoint=libs),
    Route('/pottery', endpoint=pottery),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, exception_handlers=exception_handlers, middleware=middleware, routes=routes)
