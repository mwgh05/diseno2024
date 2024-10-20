# UI

## Boilerplate

El UI se hizo mayormente a mano pero se utilizó el comando "npx create-expo-app lab-doc" para iniciar la aplicación.
Las pantallas son las siguientes:

- Home: Pantalla inicial. Solamente tiene un texto de bienvenida y un boton para iniciar.
- ExperimentForm: Tiene un text input para ingresar el procedimiento y un boton para pasar a la pantalla de grabar.
- Recording: Pantalla para grabar. Tiene botones para empezar, pausar y terminar de grabar. Al darle en terminar pasa a la pantalla de preguntas de la AI.
- AIQuestions: En esta pantalla se pueden ver las dudas de la AI. Cada una tiene su boton de resolve que lo manda a la pantalla para resolver esa duda.
- ResolveQuestions: Pantalla para resolver la duda. Tiene un text input para ingresar la respuesta.
- Documentation: En esta pantalla se visualiza la bitacora del experimento.