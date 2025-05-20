<div align='center'>
<h1>Regex Data Extraction</h1></div>

**Regular Expression** (shortened as **Regex** or **Regexp**), explained as a `sequence of characters` that specifies a `match pattern` in `text` or generally given `inputs`.Such patterns are mainly used in `string-searching algorithms`(like `find and replace` operations, used in `search engines`) and, more importantly, in `input validation`. Great thanks to  [Stephen Cole Kleene](https://en.wikipedia.org/wiki/Stephen_Cole_Kleene) for introducing the concept.

### Our task
To extract the required data from the hundreds of thousands of pages of string response you get from your API, we have decided to unleash the raw power of Regular Expressions. We already know how the specific types of data you are looking for appear in the string. This is how you have summarized that information. Now, all we have to do is write your Regular Expressions. 

In our case, we chose to work on:
- Emails
- Urls
- Phone numbers (various formats but in the context of the Country's number)
- Time (both 12-hour format and 24-hour format)
- Hashtags
- And Currency amounts(in US Dollars)
  
### Environment Setup
1. Ensure that you have **Python 3x** installed already because we used **Python** to implement all `Regex` logic.
```
# To install the colorama package used in this project

pip install -r requirements.txt
```
2. After installing [colorama](https://github.com/tartley/colorama), you have to run your program as well 🤤. The main reason we used `coloram` is to make our `CLI` program, while testing our `regex`, look nicer.

```
# Here you can use python3 or simply python
# And usually like to use Python only

Python main.py
```
So far, we are ready to use our `Regex` validator ✔️.

### How it works
<details><summary> 1. Emails</summary>
  
- Here used the pattern `\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b` to look for alphanumeric(alphabets and numbers) characters or even symbols like `.`, `_`, `%`, `+` or `-` before `@` and then after `@` we can also look for alphanumeric characters plus symbols like `.` or `-` and then look for `.` after those characters and after `.`, we can accept alphabets only from at least two characters. 
- `\b` look for any word boundary before the pattern and after.
</details>  

<details><summary>2. URLs </summary>

Here we used the pattern `\bhttps?://(?:www\.)?[\w-]+\.[\w.-]+[/\w .-]*\b` to look for links that start with `https://` followed by `www.` as the general format, or not ones like `https://rubular.com/` and be able to validate correctly the links with pages as well but not limited to letters, numbers, dots or underscores.
</details>
<details><summary>3. Phone Numbers </summary>

Here we used the pattern `[(][+]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{3}?[0-9]{3}[-\s\.]?[0-9]{3}` which allows us to validate right all the phone numbers start with `()` and in paranthesis we must have `3-numeric characters` but started with `+`, and then followed by `9-numeric characters` grouped in 3-characters where those groups can be separated by `.` or `-`.

**Examples** here can be (+123) 456-789-001, (+250) 790 068 175, or (+123).456.789.103.

> This is kinda great for `Rwanda's phone numbers` or any other country with 3-numeric characters as country codes or even phone numbers of about ten characters, but can't work well for other phone numbers.

</details>
<details><summary>4. Times </summary>
  
</details>

<details><summary>5. Hashtags </summary>
  
To be able to extract valid `hashtags`, we used `#\w+\b` as a pattern so that we can look for only characters followed by `#` with an even number or underscores in it.
</details>
<details><summary>6. Currency amounts</summary>
  
</details>

### Resources

