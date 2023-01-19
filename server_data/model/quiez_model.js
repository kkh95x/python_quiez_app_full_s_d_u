const { Console } = require('console');
const mongoose = require('mongoose');

const DB_URL = "mongodb://127.0.0.1:27017/qu"
mongoose.set('strictQuery', false);
const quiezSchema = mongoose.Schema({
    question: String,
    answers: [{ type: String }],
    
    index_of_the_correct_answer: Number
    
})
const quiezModel = mongoose.model('quiez', quiezSchema)


exports.createQiuez = (data) => {


console.log(data)
    return new Promise((resolve, reject) => {

        mongoose.connect(DB_URL).then(() => {
            
            new quiezModel({
                question: data['question'],
                answers: data['answers'],
               
                index_of_the_correct_answer: data['index_of_the_correct_answer']
            }).save().then(() => {
                resolve('saved')
                mongoose.disconnect()
            }).catch((res) => {
                reject(res)
                mongoose.disconnect()
            })

        })



    })

}



exports.getAllQuiez = () => {
    return new Promise((resolve, reject) => {
        mongoose.connect(DB_URL).then(() => {
            quiezModel.find().then((data)=>{
           
             resolve(data)
             mongoose.disconnect()
          }) .catch((er)=>{
            reject(er)
            mongoose.disconnect()
          })
        }).catch((er) => {
            reject(er)
            mongoose.disconnect()
        })


    })
}