class PC extends Device{
    static instance;

    constructor(){
        //constructor
    }

    static getInstance(){
        if(!PC.instance){
            PC.instance = new PC();
        }
        return PC.instance;
    }
    
    display(context){
        print("Renderizando en una PC");
    }
}