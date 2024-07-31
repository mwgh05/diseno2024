class Celular extends Device{
    static instance;

    constructor() {
        //constructor
    }

    static getInstance() {
        if (!Celular.instance) {
            Celular.instance = new Celular();
        }
        return Celular.instance;
    }
    display(context){
        print("Mostrando en un celular");
    }
}