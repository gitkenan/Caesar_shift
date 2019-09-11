# Caeser_shift
I created a way to encrypt and decipher text using the Caeser shift in Python 2 and a dictionary. 

## How to use this app
First download the words_alpha.txt file and caesershift2.py to the same directory.
Run with Powershell or command line. 
This programme has recently been updated to be able to encrypt and decrypt strings with
or without uppercase letters and special characters.

```
What would you like to do?
1. Encrypt
2. Decrypt
Enter your option below.
>
```

Depending on what you would like to do, type '1' or '2' and press ENTER. If you'd like
to encrypt something, next:

```
Enter the text you would like to encrypt.
> hello this is a test
```
We enter the string 'hello this is a test' without any quotation marks as the programme
will convert the text into a string automatically. Then, the programme will ask:

```
Enter the shifting constant.
> 7
```
This means we'd like to perform a Caesar shift with key 7. Then, we see the encrypted string
once we press ENTER.

```
olssv aopz pz h alza is the encrypted string.
```

Next, suppose we'd like to decrypt this back to its original form. We begin the programme again,
select option '2' and press ENTER.

```
Enter the text you would like to decrypt.
> olssv aopz pz h alza
```

When we press ENTER, we are presented with the following:

```
The decrypted string is (['hello', 'this', 'is', 'a', 'test'], 'also', 19, 'is what we shifted by')
Thank you for using this programme,
written by Kenan Al-Shamie.
```
## Built With

Credit to https://github.com/dwyl/english-words for the words_alpha.txt file which 
I pull from for this caeser cipher programme, written in Python 2.

