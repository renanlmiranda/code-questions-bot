'''
questions.py: questions to be used by tweet.py for @CodeQBot
21 January 2020
Vicki Langer (@vicki_langer)
'''

# TODO: add more questions
# NOTE: please add the question, then comment the expected answer

QUESTIONS = [
    # 'testing an automatic reply to this post',
    'What is Alan Turing known for?',  #
    'What language was used in "Stranger Things" Season 2?',  # BASIC https://moviecode.tumblr.com/post/166870949505/at-least-they-tried-basic-from-stranger-things
    'What is polymorphism?',  # A programming language feature that allows the values of different data types to be handled using a uniform interface.
    'Answer with a GIF. \nWhat is HTTP status 417?',  # Expectation Failed https://httpstatuses.com
    'Whats the difference between an editor and an IDE?',  # 
    ]

    # 'What questions would you like us to ask? Or what kinds of questions would you like to see?',  # Open-ended, no right answer
    # 'Who has been called the worlds first computer programmer?',  # Ada Lovelace
    # 'Who popularized the idea of machine-independent programming languages?',  # Grace Hopper
    # 'What is "!" used for in "!=" ?',  # Not
    # 'What is required in the HTML <head>?',  # charset, viewport, title https://htmlhead.dev
    # 'What’s difference between The Internet and The Web?',  # hardware vs software
    # 'What characters do you use to comment your code? What language are you using?',  # Depends on the language
    # 'Why does List, the language,  use () instead of []?',  # The keyboard used to develop had issues with the [ key
    # 'What does Wi-Fi stand for?',  # nothing https://www.webopedia.com/DidYouKnow/Computer_Science/wifi_explained.asp
    # 'What is 0.1 + 0.2 in your language? Why?',  # https://0.30000000000000004.com/
    # 'Whats the difference between an editor and an IDE?',  # 
    # 'ELI5: What is the DOM?',  # https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model
    # 'ELI5: What is debugging?',  # 
    # 'ELI5: What are the APIs?',  # https://developer.mozilla.org/en-US/docs/Web/API
    # 'ELI5: What is Git?',  #
    # 'ELI5: What is an IDE?',  #
    # 'ELI5: "=" != "==" != "==="',  #
    # 'What is Alan Turing known for?',  #
    # 'What is Open Source Software (OSS)?',  #
    # 'What does it mean to be "Turing complete"?',  #
    # 'What is an instance and what does it mean to instantiate?',  #
    # 'What is the difference between high-level and low-level languages?',  #
    # 'What was the first song ever sung by a computer?',  # "Daisy Bell" was composed by Harry Dacre in 1892. In 1961, the IBM 7094 became the first computer to sing, singing the song Daisy Bell
    # 'What is polymorphism?',  # A programming language feature that allows the values of different data types to be handled using a uniform interface.
    # 'What is the name of the Java mascot?',  # Duke
    # 'What\'s the story behind the first computer virus?',  # http://web.eecs.umich.edu/~aprakash/eecs588/handouts/cohen-viruses.html
    # 'What was the first computer bug?',  # an actual bug
    # 'In a tree, where is the root?',  # The top
    # 'In terms of coding: when may a parent kill a child?',  # if the task assigned to them is no longer needed
    # 'Who recorded the first computer bug? What were they doing?',  # Grace Hopper recorded the first computer ‘bug’ in the book as she was working for the MARK II computer. https://www.nationalgeographic.org/thisday/sep9/worlds-first-computer-bug/

    # Language Creation
    # 'How was the language Java invented?',  # James Gosling, at Sun Labs, around 1992; the group was building a set-top box and started by “cleaning up” C++ and wound up with a new language and runtime.
    # 'What was PHP initially created for?',  # Lerdorf had created the language, or interface at the time, for the purpose of managing his personal website.
    # 'What was Java initally design for?',  # Java was designed with the primary aim for use in Interactive television
    # 'Where did the language "C" get it\'s name?',  # C language succeeds B language
    # 'Who is the creator of JavaScript?',  # Brendan Eich
    # 'What was Java called before it was Java? \nextra points: why was it changed?',  # Oak. Thename was ruled out by Sun's trademark lawyers since the name was used by the company Oak Technologies
    # 'What programming language did Bjarne Stroustrup create?',  # C++
    # 'Where did the language "Python" get it\'s name?',  # creator liked the movie Monty Python

    # Movies and TV
    # 'What language was on Arthur\'s Heads Up Display (HUD) in "Ralph Breaks the Internet"?',  # https://www.reddit.com/r/Python/comments/ariypt/just_noticed_that_the_code_in_ralph_breaks_the/
    # 'What language was used in "Stranger Things" Season 2?',  # BASIC https://moviecode.tumblr.com/post/166870949505/at-least-they-tried-basic-from-stranger-things
    # 'In "Doctor Who" Season 7 Episode 2, what code is guiding the missiles?',  # In Doctor Who S07E02, missiles are being guided by the power of SVGs.
    # 'In "Silicon Valley" Season 3 Episode 1, what language is being used?',  # https://www.reddit.com/r/SiliconValleyHBO/comments/4gbra7/i_got_the_silicon_valley_s03e01_code_to_compile/)

    # HTTP Statuses
    # 'Answer with a GIF. \nWhat is HTTP status 100?',  # Continue https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 101?',  # Switching Protocols https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 102?',  # Processing https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 200?',  # Okay https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 201?',  # Created https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 202?',  # Accepted https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 300?',  # Multiple Choices https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 301?',  # Moved Permanently https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 302?',  # Found https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 305?',  # Use proxy https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 307?',  # Temporary Redirect https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 308?',  # Permanent Redirect https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 400?',  # Bad Request https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 401?',  # Unauthorized https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 402?',  # Payment Required https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 403?',  # Forbidden https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 404?',  # Not Found https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 417?',  # Expectation Failed https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 418?',  # I'm a teapot https://httpstatuses.com
    # 'Give an example of HTTP status 418, in the wild. Screenshots encouraged',  # google has one
    # 'Where did HTTP status 418 come from?',  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418
    # 'Answer with a GIF. \nWhat is HTTP status 500?',  # Internal Server Error https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 503?',  # Service Not Available https://httpstatuses.com
    # 'Answer with a GIF. \nWhat is HTTP status 508?',  # Loop Detected https://httpstatuses.com
