sum=0;
process.argv.forEach(function(val,index,array) {
        if (index >= 2) {
                sum+= val*val;
        }
});
console.log(sum);
