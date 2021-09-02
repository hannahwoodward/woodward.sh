from frontmatter import Frontmatter
from pathlib import Path
from starlette.applications import Starlette
from starlette.middleware import Middleware
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

async def archive(request):
    posts = []
    for p in Path('data/archive').glob('*.md'):
        slug = re.sub(r'data/archive/(.+)\.md', r'\g<1>', str(p))
        post = get_entry_data('archive/' + slug, slug)
        if post and post['metadata']['enabled']:
            posts.append(post)

    template_vars = {
        'request': request,
        'entry': {
            'posts': posts,
            'title': 'Archive'
        }
    }

    return templates.TemplateResponse('archive.jinja', template_vars)

async def archive_entry(request):
    slug = request.path_params['slug']

    template_vars = {
        'request': request,
        'entry': get_entry_data('archive/' + slug, slug)
    }

    return templates.TemplateResponse('_entry.jinja', template_vars)

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

routes = [
    Route('/', endpoint=index),
    Route('/archive', endpoint=archive),
    Route('/archive/{slug}', endpoint=archive_entry),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, exception_handlers=exception_handlers, routes=routes)
