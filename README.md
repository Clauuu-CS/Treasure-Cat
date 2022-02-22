# Cat's Treasure Hunt- Game
by Clàudia Sallés

## :pencil: Description:
This project is a game used to experiment with the possibilities that the Ren'Py framework allows. It follows the structure of a visual novel, with various endings depending on the options chosen. It experiments with the use of backgrounds, different states of a character and story stucture. 

## :woman_student: Things I leaned:
- Overall understanding of the Ren'Py framework.
- How to create and jump to different scenarios with the label function.
- How to create a script with various caracters that have a defined text.
- Displayment of images and backgrouds, along with a variety of effects for transitioning.

## :woman_teacher: Things I can teach: 
- **Opening and closing eye effect:** The use of two different backgrounds to create the effect of the user opening and closing their eyes, as if they were waking up or going to sleep.
```Python
scene bg eye with fade      ## bg eye: a black shape of an eye half closed with the character already begind it.
scene bg black with fade    ## bg black: completely black backgroud that simulates fully closed eyes.

c "Hey you!"

scene bg eye with fade
scene bg black with fade
```

- **Method to have a non-instant response after a question:** Through this method the user has no information about what question they answered correctly or incorrectly, forcing them to have to repeat a certain phase until all the choices they pick are the good answer. It gets only one of the questions to be answered wrong for the conditional that leads to the wrong_answer ending to be triggered.
```Python
label start:
  $ wrong = False ## Variable "wrong" is reseted every time the phase starts to prevent any previous errors to influence the current run.
  $ right = True
      menu:
          "Option1":
              $ wrong = True
          "Option2":
              $ wrong = True
          "Option 3":
              $ wrong = True
          "Option 4":
              ## right answer
              $ right = True
          "Option 5":
              $ wrong = True
      menu:
          "Option1":
              $ wrong = True
          "Option2":
              ## right answer
              $ right = True
          "Option 3":
              $ wrong = True
          "Option 4":
              $ wrong = True
          "Option 5":
              $ wrong = True
      menu:
          "Option1":
              $ wrong = True
          "Option2":
              $ wrong = True
          "Option 3":
              $ wrong = True
          "Option 4":
              $ wrong = True
          "Option 5":
              ## right answer
              $ right = True

      if wrong == True:     ## This conditional will trigger if at least one of the questions is answered incorrectly. 
        jump wrong_answer

      if wrong == False:    ## This conditional may only trigger if all the questions are answered correctly.
        jump good_answer
```



## 	:notebook_with_decorative_cover: Bibliography:
### Code tutorials and forums:
- [Displaying images](https://www.renpy.org/doc/html/displaying_images.html)
- [Numbers as Variables in a Text](https://www.renpy.org/wiki/renpy/doc/reference/Text#Interpolation)
- Ren'Py tutorial (how to operate text and images)

### Audio:
(None used yet)

### Images:
(All images are original)

