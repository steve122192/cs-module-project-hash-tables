import re

def word_count(my_str):

  my_str = my_str.lower()
  my_str = my_str.split(' ')
  words = {}
  for word in my_str:
    new_word = re.sub(r"[^a-zA-Z0-9]+", '', word)
    if new_word not in words:
      words[new_word] = 1
    else:
      words[new_word] += 1
  return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))