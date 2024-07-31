/**
 * @type {{ [key: string]: Device }}
 */
const devices = {};

devices['Celular'] = Celular.getInstance();
devices['Pc'] = PC.getInstance();
devices['Tablet'] = Tablet.getInstance();

function display(req, res){
    try {
        const {id, context, device} = req.params;

        if (!id || !context || !value) {
            res.status(400).send('Faltan parametros');
            return;
        }

        const request = new Request(context, device);
        ServerSideRender.getInstance().display(devices[request.device], request);
    }catch(e){
        res.status(500).send('Error interno');
    }
}
