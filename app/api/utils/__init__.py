#constants

FREE_TIRE_CHARACTERS_LIMIT = 5000
PAIED_TIRE_CHARACTERS_LIMIT = 1000*100


DEFAULT_SUMMARY_LANGUAGE = "en"
CHUNK_SIZE = 2500
CHUNK_OVERLAP = 20




SUMMARY_PROMPTS = {
    "en": '''
You are an expert writer, your task is to write consice summry of a given text. make sure to structure your summary in this way:
<<structure>>

Title 

- 1st point:
  paragraphe explaining the first point in clear details.

- 2nd point: 
  paragraphe explain the second point in clear details.

etc ...

- conclusion: 
  paragraph that conclude a resume of all points.


<<{text}>>

--------
write a summary with respect to the structure mentioned above!

<<summary>>

''',

    "fr": '''
Vous êtes un écrivain expert, votre tâche consiste à rédiger un résumé concis d'un texte donné. assurez-vous de structurer votre résumé de cette façon :
<<structuration>>

Titre

- 1er point :
   paragraphe expliquant le premier point avec des détails clairs.

- 2ème point :
   paragraphe expliquent le deuxième point avec des détails clairs.

etc ...

- conclusion:
   paragraphe qui conclut un résumé de tous les points.


<<{text}>>

--------
rédigez un résumé par rapport à la structure mentionnée ci-dessus !

<<résumé>>
''',
}




QUIZ_PROMPTS = {
    "fr":'''
            Donner un quiz sur le text ci-dessus avec 3  question possible.
            Renvoie le quiz au format sériable a json (avec comme clés le numéro de la question entre guillemets doubles et la valeur comme "Q":(la question),"A":(la réponse valide), "choices":(liste de 3 choix incluant la réponse valide))\n
            <<{text}>>
            
            <<quiz>>

          ''',
    
    "en":'''
          Give a quiz on the text below with 3 possible questions. 
          Return the quiz in the a json seriable format (with keys as the number of the question in double quotes and the value as "Q":(the question), "choices":(list of 3 choices including the valide respone),"A":(the valide answer))\n
          --------
          <<{text}>>

          <<quiz>>
          
        '''
}



FLASHCARDS_PROMPTS = {
    "fr":'''
            Donner 3 flashcards possible sur le text ci-desous.
            Retourner le quiz sous le form json suivant :\n
            Renvoie le flashcards au format sériable a json (avec comme clés le numéro de la card entre guillemets doubles et la valeur comme "Q":(la question),"A ":(la réponse valide))\n
            --------
            <<{text}>>
            
            <<quiz>>
          ''',
    
    "en":'''
          Give 3 flashcards on the text below. 
          Return the flashcards in the a json seriable format (with keys as the number of the card in double quotes and the value as "Q":(the question), "A":(the valide answer))\n
          --------
          <<{text}>>

          <<quiz>>
        '''
}






