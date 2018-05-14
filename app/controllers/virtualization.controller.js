var PythonShell = require('python-shell');
var plotly=require('plotly')('diaaahmed850', '83NoyArxBnAAAM7tn1K4');
var fs = require('fs');
exports.visualize_users_diaa = (req, res) => {
    console.log("done");
    PythonShell.run('shit.py', function (err, results) {
        if (err)
            res.send(err)
                User.find({}).exec((err, user) => {
                    if (err)
                        res.send(err);
                     
                    console.log("done");
                    
                    res.render('visualization/users_diaa', { 'users': user, 'user_id': JSON.parse(localStorage.getItem('user')).name });
                });

           
        console.log("done");
         
    });
};
 
exports.redraw = (req, res) => {
    var options = {
        
        args: req.params.userName
    };
    console.log("done");
    PythonShell.run('shit.py', options,function (err, results) {
        if (err)
            res.send(err)
        User.find({}).exec((err, user) => {
            if (err)
                res.send(err);

            console.log("done");
            res.render('visualization/users_diaa', { 'users': user, 'user_id': JSON.parse(localStorage.getItem('user')).name });
        });


        console.log("done");

    });

};
exports.visualize_users = (req, res)=>{
  User.find({}).populate('friends').exec((err, user)=>{
      if (err)
          res.send(err);
          console.log(JSON.parse(localStorage.getItem('user')).name);

      res.render('visualization/users',{'users':user,'user_id':JSON.parse(localStorage.getItem('user')).name});
  });

};
exports.stat = (req, res) => {
    
    console.log("done");
    PythonShell.run('diaa.py', function (err, results) {
        if (err)
            res.send(err)
        Group.find({}).exec( (err, groups) => {
            if (err) {
                res.send(err);
            }
            console.log(groups)
            res.render('visualization/stat', { 'groups': groups,'flag':0 })
        });
         

             
        });


        console.log("done");

     
    
    
};
exports.stat_redraw = (req, res) =>{
    console.log(req.params.groupid)
    var options = {

        args: req.params.groupid
    };
    console.log("done");
    PythonShell.run('diaa.py',options, function (err, results) {
        if (err)
            res.send(err)
        Group.find({}).exec((err, groups) => {
            if (err) {
                res.send(err);
            }
             
            res.render('visualization/stat', { 'groups': groups, 'flag': 1, 'gnmae': req.params.groupid })
        });



    });


    console.log("done");




};
