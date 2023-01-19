const { Console } = require('console');
const mongoose = require('mongoose');

const DB_URL = "mongodb://127.0.0.1:27017/qu"
const marksSchema = mongoose.Schema({
    id: String,
    username:String,
    avg: String,
    dateTimeForSoultion:String
    
})
const marksModel = mongoose.model('marks', marksSchema)


exports.createMarks = (data) => {


    console.log(data)
    return new Promise((resolve, reject) => {

        mongoose.connect(DB_URL).then(() => {
            
            new marksModel({
                id: data['id'],
                username: data['username'],
                avg:data['avg'],
                dateTimeForSoultion: data['dateTimeForSoultion']
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



exports.getAllmarks = () => {
    return new Promise((resolve, reject) => {
        mongoose.connect(DB_URL).then(() => {
            marksModel.find().then((data)=>{
           
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