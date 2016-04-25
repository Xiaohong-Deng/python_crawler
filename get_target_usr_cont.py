from bs4 import BeautifulSoup
# import re

# if function passed to BS obj alone, default arg passed to the func is the tag itself
# if the func is given to a specific attr, like this
# soup.find_all('a', href=funcname)
# then the attr's value will be passed in as arg

def msg_or_author(tag):
  if tag.name == 'div' and tag.has_attr('class'):
    return tag.get('class') == ['postmessage',''] or tag.get('class') == ['postmessage', 'firstpost']
    if tag.name == 'td' and tag.has_attr('class') and tag.has_attr('rowspan'):
      return tag.get('class') == ['postauthor']
      return False

if __name__ == "__main__":
  file = 'd:\GitProject\web_crawler\sample.html'
  message = []
  authors = []
  with open(file, 'r') as f:
    thd_cont = BeautifulSoup(unicode(f.read(), "utf-8"))
  # raw_msg_author = thd_cont.find_all('div', class_="postmessage ")
  # des_1st = raw_messages[0].descendants
  # print type(des_1st)
  # for child in des_1st:
    # print child

  # class_ is a special case for class attr I dont know why
  # Normally it's just attr name such as 'target' for target attr
  
  # raw_msg_author = thd_cont.find_all('td', class_="postauthor")
  raw_msg_author = thd_cont.find_all(msg_or_author)
  
  target_usr_msg = []

  read_cont = False
  for tag in raw_msg_author:
    if tag.name == 'td':
      author = tag.find('a', target="_blank").get_text()
      if author == 'xufengwd':
        read_cont = True
        continue
    else if read_cont:
      cont = tag.find('table', cellspacing="0").get_text()
      target_usr_msg.append(cont)
      read_cont = False

  for m in target_usr_msg:
    print m
  # for m in raw_msg_author:
    # print m.get('class')

  # raw_second_author = raw_msg_author[2]
  # second_author_str = raw_second_author.find('a', target="_blank").get_text()
  # print second_author_str

  # raw_second_message = raw_msg_author[3]
  # second_message_str = raw_second_message.find('table', cellspacing="0").get_text()
  # print second_message_str

  # print raw_msg_author[0].has_attr('class')
  # print raw_msg_author[1]['class'] #== "postmessage "