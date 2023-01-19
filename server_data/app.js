const express = require('express')
const quiezModel=require('./model/quiez_model')
const marksModel=require('./model/mark_model')

const bodyParser=require('body-parser')
const app = express()
const port = 3000




app.use(express.urlencoded({ extended: false }));
app.use(bodyParser.json());


app.get('/', (req, res) => {
  

  quiezModel.getAllQuiez().then((quiez)=>{
    res.json({
      'quiez':quiez
    })
  })
})


app.post('/add',bodyParser.urlencoded({extended:true}),(req, res) => {


  quiezModel.createQiuez(req.body).then(()=>{
    res.json({
      'data':'added'
    })
  }).catch((er)=>{
    res.json(er)
  })


})
app.post('/marks',bodyParser.urlencoded({extended:true}),(req, res) => {


  marksModel.createMarks(req.body).then(()=>{
    res.json({
      'data':'added'
    })
  }).catch((er)=>{
    res.json(er)
  })


})
app.get('/marks', (req, res) => {
  

  marksModel.getAllmarks().then((marks)=>{
    res.json({
      'quiez':marks
    })
  })
})


app.listen(port, () => {
  console.log(`Example app listening http://localhost:${port}/`)
})