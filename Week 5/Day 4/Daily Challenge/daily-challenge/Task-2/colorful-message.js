const chalk = require('chalk');
function displayColorfulMessage(){
    const message =chalk.yellow.bold('Hello Oumaima')
    console.log(message);
}
module.exports=displayColorfulMessage;