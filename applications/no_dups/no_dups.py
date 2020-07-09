def no_dups(my_str):
  new_str = ''
  words = {}
  my_str = my_str.split(' ')
  for word in my_str:
    if word not in words:
      words[word] = 1
      new_str += ' ' + word
  if new_str[0] == ' ':
    new_str = new_str[1:]
  return new_str



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))