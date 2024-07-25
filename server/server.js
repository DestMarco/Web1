/*npm install --save-dev express cors*/
/*Per evitare di riavviare: npm i nodemon 
npx nodemon --exec node server.js*/

const express = require('express');
const cors = require('cors')

/*
const multer = require("multer");
const upload = multer({ dest: "uploads/" });
*/

const app = express();

app.use(cors());

var iPortaTcp = 4201;
var sIpAddress = "127.0.0.1"

app.listen(iPortaTcp,sIpAddress, () => console.log('API is running on http://' + sIpAddress + ':' + iPortaTcp));
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));

//*********** 
//ROUTING
//*********** 

app.get('/formRegistrazione', (req, res) => {
console.log("Mi hai chiesto di salutarti");
//res.send("<html>Buonanotte al secchio 18 06 2024</html>");
res.sendFile("formSemplice.html", { root: './htdoc' });
});


app.get('/sendFile', (req, res) => {
    console.log("Mi hai chiesto la form di invio del file");
    res.sendFile("sendfile.html", { root: './htdoc' });
    });



//GESTIONE DELLA URL MANSENDFILE
/*
app.post('/mansendfile', (req, res) => {
    
    console.log(req.body.password)
    pass_ricevuta = req.body.password;
    if(pass_ricevuta=="paperino")
        res.send("<html>Bravo " + req.body.email + "<br>Sono pronto a ricevere il file!</html>")
    else
        res.send("<html>Attenzione, password errata!!</html>")
});
*/
//app.post("/mansendfile", upload.single("file"), uploadFiles);

function uploadFiles(req, res) {
    console.log(req.body);
    console.log(req.file);
    res.send("<html>File ricevuto correttamente</html>")
}


/*
app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname,req.query.fcognome);
    res.send("<html>Buona serata " + req.query.fname + " " + req.query.fcognome + "</html>");
    });
*/
app.get('/gestisciDatiForm', (req, res) => {
    console.log(req.query.fname, req.query.fcognome);
    response="<html>Buona serata " + req.query.fname + " " +  req.query.fcognome ;
    response+="la tua città e " + req.query.fComune 
    if(req.query.fsesso == "1")
        response += "<br> sei un maschio"
    else
        response +="<br> sei una femmina"
    response +="<br> ti voglio bene " + "</html>"
    res.send(response)
    }); 
    

app.post('/gestisciDatiForm', (req, res) => {
    console.log(req.body.fname, req.body.fcognome);
    response="<html>Buona mattinata " + req.body.fname + " " +  req.body.fcognome ;
    response+="<br>la tua città e " + req.body.fComune 
    if(req.body.fsesso == "1")
        response += "<br> sei un maschio"
    else
        response +="<br> sei una femmina"
    response +="<br> ti voglio bene " + "</html>"
    res.send(response)
    }); 
    
