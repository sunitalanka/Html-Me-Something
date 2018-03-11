def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    name_str = fullname

    n_list = name_str.split()

    nick_name = ''

    for name in n_list:

            nick_name = nick_name + name[0]

    return nick_name.upper()


def main():
    n_m = input("What is your name:")
    print ("The initials of", n_m ,"are", get_initials(n_m))
if __name__=="__main__":
     main() 