'''
Module for checking "cache_webpage.py" module.
'''
from urllib.request import urlopen
import time
from cache_webpage import WebPage


def get_data():
    '''
    Gets data from the user.
    '''
    url = input('URL: ')
    reload_time = int(input('Reload time: '))
    time_to_sleep = int(input('Delay between your requests to webpage: '))

    output = {'url': url, 'reload_time': reload_time, 'sleep': time_to_sleep}

    return output


def cache_test():
    '''
    Simulates situation with webpage cache reloading and shows whether the webpage was reloded.
    '''
    data = get_data()
    url = data['url']
    reload_time = data['reload_time']
    sleep_time = data['sleep']

    webpage = WebPage(url, reload_time)

    now = time.time()
    content1 = webpage.content
    time_before = time.time() - now
    print('Reload lasted {0:.3f}\n'.format(time_before))

    time.sleep(sleep_time)

    if sleep_time >= webpage.reload_time:
        print("Your webpage was reloaded.")
        now = time.time()
        content2 = webpage.content
        time_after = time.time() - now
        print('Reload lasted {0:.3f}\n'.format(time_after))
    else:
        print('Your webpage was cached and we you will get it without reloading.\n')
        content2 = content1

    with open('task_3/webpage.html', 'w') as webpage:
        webpage.write(str(content2))
        webpage.close()

    print(f'Check your final version of webpage in "webpage.html" file.')


if __name__ == "__main__":
    cache_test()
