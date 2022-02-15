# Treasure Cat - Game
by Clàudia Sallés

## Things I leant:
- How to 
```
label start:
  $ wrong = False
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

      $ if wrong == True:
          jump start

      $if wrong == False:
          jump continuation
```

## Things I can teach: 

## Things I leant:
(All images and code was made by me)
