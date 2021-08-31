from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

async def index(request):
    template_vars = {
        'request': request,
        'entry': {
            'title': 'About'
        }
    }

    return templates.TemplateResponse('index.jinja', template_vars)

async def archive(request):
    template_vars = {
        'request': request,
        'entry': {
            'title': 'Archive'
        }
    }

    return templates.TemplateResponse('archive.jinja', template_vars)

async def archive_entry(request):
    slug = request.path_params['slug']

    template_vars = {
        'request': request,
        'entry': {
            'title': ''
        }
    }

    return templates.TemplateResponse('_entry.jinja', template_vars)

async def error_404_not_found(request, exc):
    template_vars = {
        'request': request,
        'entry': {
            'title': '404 - Not Found'
        }
    }

    return templates.TemplateResponse('_error.jinja', template_vars, status_code=exc.status_code)

async def error_500_server(request, exc):
    template_vars = {
        'request': request,
        'entry': {
            'title': '500 - Server Error'
        }
    }

    return templates.TemplateResponse('_error.jinja', template_vars, status_code=exc.status_code)


exception_handlers = {
    404: error_404_not_found,
    500: error_500_server
}

routes = [
    Route('/', endpoint=index),
    Route('/archive', endpoint=archive),
    Route('/archive/{slug}', endpoint=archive_entry),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, exception_handlers=exception_handlers, routes=routes)
