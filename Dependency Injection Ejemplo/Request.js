class Request{
    context;
    device;
    constructor(context, device){
        this.context = context;
        this.device = device;
    }

    get context(){
        return this.context;
    }
    
    /**
     * @param {string} value
     */
    set context(value){
        this.context = value;
    }

    get device(){
        return this.device;
    }

    /**
     * @param {string} value
     */
    set device(value){
        this.device = value;
    }
}
