---
toc: true
layout: post
description: A minimal example of using markdown with fastpages.
categories: [markdown]
title: My example Markdown Post
---
# Example Markdown Post

## Basic setup

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-filename.md`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `filename` is whatever file name you choose, to remind yourself what this post is about. `.md` is the file extension for markdown files.

The first line of the file should start with a single hash character, then a space, then your title. This is how you create a "*level 1 heading*" in markdown. Then you can create level 2, 3, etc headings as you wish but repeating the hash character, such as you see in the line `## File names` above.

## Basic formatting

You can use *italics*, **bold**, `code font text`, and create [links](https://www.markdownguide.org/cheat-sheet/). Here's a footnote [^1]. Here's a horizontal rule:

---

## Lists

Here's a list of my favorite sports to play:

1. Football
2. Basketball
3. Track and Field

## Boxes and stuff

> This is a quotation

{% include alert.html text="You can include alert boxes" %}

...and...

{% include info.html text="You can include info boxes" %}

## Images
###### 49ers Logo
![](https://loodibee.com/wp-content/uploads/nfl-san-francisco-49ers-team-logo.png)



## Code

You can format text and code per usual 

General preformatted text:

    # Do a thing
    do_thing()

#### Python Code Embeds:
Addition and Subtraction Calculator

```python
num_1 = input('Enter your first number: ')
num_2 = input('Enter your second number: ')

num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
 
# Addition
print('{} + {} = '.format(num_1, num_2))
print(num_1 + num_2)
 
# Subtraction
print('{} - {} = '.format(num_1, num_2))
print(num_1 - num_2)

Formatting text as shell commands:

```shell
echo "hello world"
./some_script.sh --option "value"
wget https://example.com/cat_photo1.png
```

Formatting text as YAML:

```yaml
key: value
- another_key: "another value"
```


## Tables

| First Name | Last name |
|-|-|
| LeBron | James |
| Tom | Brady |
| Lionel | Messi |


## Tweetcards

{% twitter https://twitter.com/elonmusk/status/1557957132707921920?s=20&t=kcohacnpMaPNzlzVjXEl4g %}


## Footnotes



[^1]: This is my footnote. Markdown is a markup language in which you can add formatting elements to plaintext text documents. 

