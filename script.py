keyword = input('Enter a keyword: ')
def search_videos_by_keyword(service, **kwargs):
    results = service.search().list(**kwargs).execute()
    for item in results['items']:
        print('%s - %s' % (item['snippet']['title'], item['id']['videoId']))

keyword = input('Enter a keyword:  ')
search_videos_by_keyword(service, q=keyword, part='id,snippet', eventType='completed', type='video')
