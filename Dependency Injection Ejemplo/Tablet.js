class Tablet extends Device{
    static instance;

    constructor(){
        //constructor
    }

    getInstance(){
        if(!Tablet.instance){
            Tablet.instance = new Tablet();
        }
        return Tablet.instance;
    }

    display(context){
        print("Renderizando en una Tablet");
    }
}