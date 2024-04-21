print('Start!')
import mechanicalsoup
import configparser
import datetime

print(datetime.datetime.now())

#browser object
browser = mechanicalsoup.StatefulBrowser()
#print(browser)

#config object
config = configparser.ConfigParser()

#open login page
page = browser.open("https://teveclub.hu/")
#print(page)

#find loginform
login_form = browser.select_form('form[name=\"loginform\"]')
#print(login_form)
#login_form.print_summary()

#config read
config.read('creds.ini')
#print(config.sections())

#set input field values
browser['tevenev'] = config['teveclub.hu']['tevenev']
browser['pass'] = config['teveclub.hu']['pass']

#login_form.print_summary()

# Submit loginform
response = browser.submit_selected() 
'''
print('-----------------------------')
print(response.text)
'''

#find etet form
try:
    etet_form = browser.select_form('form[name=\"etet\"]')
    #print(etet_form)
    #etet_form.print_summary()

    etet = browser.submit_selected()
    print('Etetés kész!')
    del etet, etet_form
except:
    print('Nem kell etetni!')

#open tanit page
page = browser.open("https://teveclub.hu/tanit.pet")
#print(page)

#find tanitb form
try:
    tanitb_form = browser.select_form('form[name=\"tanitb\"]')
    #print(tanitb_form)
    #tanitb_form.print_summary()

    tanit = browser.submit_selected()
    print('Tanítás kész!')
    del tanit, tanitb_form
except:
    print('Ma már tanult a teve!')


#open egyszam page
page = browser.open("https://teveclub.hu/egyszam.pet")

#find egyszam form
try:
    egyszam_form = browser.select_form('form[name=\"egyszam\"]')
    browser['honnan'] = config['teveclub.hu']['tipp']
    #print(egyszam_form)
    #egyszam_form.print_summary()
    
    tipp = browser.submit_selected()
    print('Tippelés kész!')
    del tipp, egyszam_form
except:
    print('Ma már tippelt a teve!')

del page, response, config, browser
print('Kész!')


    
