
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