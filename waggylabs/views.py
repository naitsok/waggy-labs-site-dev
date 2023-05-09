from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse
from django.shortcuts import render

from wagtail.models import Page
from wagtail.search.models import Query
from wagtail.search.utils import parse_query_string

from waggylabs.utils import get_tokens_from_query


def search(request):
    # Get search query
    query_string = request.GET.get('query', None)
    
    # Parse search query
    filters, query = parse_query_string(query_string, operator='or')
    
    
    if query:
        search_results = Page.objects.live().specific().search(query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(query_string).add_hit()
    else:
        search_results = Page.objects.none()
        
    search_results = list(search_results)
        
    # # Pagination
    # paginator = Paginator(search_results, 10)
    # try:
    #     search_results = paginator.page(page)
    # except PageNotAnInteger:
    #     search_results = paginator.page(1)
    # except EmptyPage:
    #     search_results = paginator.page(paginator.num_pages)

    # Render template
    return render(request, 'waggylabs/search/search.html', {
        'search_query': query_string,
        'search_tokens': get_tokens_from_query(query),
        'search_results': search_results,
    })
