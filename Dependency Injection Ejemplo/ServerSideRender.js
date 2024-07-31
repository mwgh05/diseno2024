class ServerSideRender {
    static instance;
    
    constructor(){
        //constructor
    }

    static getInstance(){
        if(!ServerSideRender.instance){
            ServerSideRender.instance = new ServerSideRender();
        }
        return ServerSideRender.instance;
    }

    /**
     * @param {Device} device, @param {Request} request
     */
    display(device, request){
        device.display(request.context);
    }
}