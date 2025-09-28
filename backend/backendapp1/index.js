const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res)=>{
    res.send('Hello Vishwas')
})

app.get('/app', (req, res)=>{
    res.send('Hello Vishwas, welcome to the app')
})

app.listen(port, ()=>{
    console.log(`Application Listening on port ${port}`)
})