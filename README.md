
# FlipBook

This is a compiler (just a lexer and parser) for a language Flip. This can be used to create a flipbook, just like Darsheel did in Taare Zameen Par :p. A flipbook is a sequence of images when flipped fast enough looks like a movie.


## Installation

Clone the github and run the following commands

```bash
  cd flipbook/
  pip3 install -r requirements
```

Now run to build a binary from source
```bash
  make build
```
## Demo
Make sure you've followed steps in Installation section before you play around.\
To create a flipbook, create a file your_file_name.flip with contents as below:

```bash
  01 02 a.jpg
  03 04 a.jpg //shivansh
```

Each line is of the form **(start_page, end_page, image)**.
Also there should not be a skipped page. If you try to, it will show an error.
Also the image should be in **images/** directory.\
\
To compile and run this source program run:

```bash
  ./fc your_file_name.flip -o outputfile.pdf
```

Once you run this, *fc* will read the source program and will generate outputfile.pdf
in **outputs/** directory. If you do not provide the argument with -o flag, a default required.pdf will be generated.
\

To clean the build, run

```bash
  make clean
```

## Why I chose to use to use lex and yacc?

The task at hand can be done by just reading the file line by line, splitting by spaces and using if-else statements.\
The reason I chose to use lex and yacc for defining a language is if we were to design a language
with complex rules, with just reading and using if-else statements, it would be a nightmare
for the developer to manage. With lex we can define tokens for our language by regular expressions
and can add them as a plugin (see src/Lexer.py). With yacc (parser) we can define rules which
govern the syntax and semantics of our language. If I have to insert another valid statement, I will just
add another rule to our grammar (see src/Parser.py).

## What more primitives can be there?

For us to be able to generate a flipbook with apple falling on Newton's head,
we can achieve it in two different ways:
1. Create multiple images by editing corresponding to different frames and generate a flipbook by using the above compiler. Not so elegant, isn't it?
2. Create more primitives. Some of them can be :
a. **Start_page End_page image1 width height from to image2**  --- This can be a valid statement. Width, height denotes the width and height of the image1 to be inserted and **from** and **to** can be a string signifying the position like center-top, center-bottom. This inserts the image1 on top of image2 moving it proportionally from **from position** to **to position** for each page in **start_page** to **end_page**\
b.**flipbook1.pdf flipbook2.pdf** --- This can be used to merge two flipbooks by checking if they have same number of pages and placing images of flipbook1 on top of flipbook2.\
\
Note that we just need to write the rules for these statements in src/Parser.py and accordingly the business logic to handle in src/fc.py.

## Time this took

It took me around 3-4 hours in different sittings to complete this. Most of the time was taken by this README you're reading and googling about how to write valid regular expressions in python.


