from django.shortcuts import render
from django.http import HttpResponse
import arxiv


# Create your views here.
def index(request):
    return HttpResponse(content="Europe Trips")


def arxiv10(request):
    return HttpResponse(content=result)


# Construct the default API client.
client = arxiv.Client()

# Search for the 10 most recent articles matching the keyword "quantum."
search = arxiv.Search(
    query="LLM", max_results=10, sort_by=arxiv.SortCriterion.SubmittedDate
)

### Past Week

results = client.results(search)
print(results)
result_list = list(results)
result_list = [r.title for r in result_list]
for r in result_list:
    print(r)
