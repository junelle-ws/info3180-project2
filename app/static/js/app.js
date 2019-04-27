/* Add your Application JavaScript */
Vue.component('app-header', {
    template: `
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <a class="navbar-brand" href="#">Photogram</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
    
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <router-link class="nav-link" to="/">Home <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/explore">Explore <span class="sr-only">(current)</span></router-link>
          </li>
          <li class="nav-item active">
            <router-link class="nav-link" to="/users/{user_id}">My Profile <span class="sr-only">(current)</span></router-link>
          </li>
        </ul>
      </div>
    </nav>
    `
});

Vue.component('app-footer', {
    template: `
    <footer>
        <div class="container">
            <p>Copyright &copy; Flask Inc.</p>
        </div>
    </footer>
    `
});

const Home = Vue.component('home', {
   template: `
    <div class="jumbotron">
        <h1>Project 2</h1>
        <p class="lead">Welcome to Photogram!</p>
    </div>
   `,
    data: function() {
       return {}
    }
});

const Register = Vue.component('register', {
   template: `
    <div class="regis">
        <h1>Registration</h1>
        <p>Register for your account</p>
        <hr>
        
        <form id="regisForm" @submit.prevent="Register" method="POST" enctype="multipart/form-data">
            <label for="username"><b>Username</b></label>
            <input type="text" placeholder="Create username" name="username" required>
            
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>
            
            <label for="firstname"><b>Firstname</b></label>
            <input type="text" placeholder="Add Firstname" name="firstname" required>
            
            <label for="lastname"><b>Lastname</b></label>
            <input type="text" placeholder="Add Lastname" name="lastname" required>
            
            <label for="email"><b>Email</b></label>
            <input type="text" placeholder="Enter Email" name="email" required>
        
            <label for="location"><b>Location</b></label>
            <input type="text" placeholder="Where are you from?" name="location" required>
            
            <label for="biography"><b>Biography</b></label>
            <input type="textarea" placeholder="Tell us about yourself" name="bio" required>
            
            <label for="email"><b>Email</b></label>
            <input type="text" placeholder="Enter Email" name="email" required>
            
            <label for="photo"><b>Profile Picture</b></label>
            <input type="file" name="pic" id="photo" required>
            
            <button type=submit class="btn btn-primary" > Register </button>
        </form>
    </div>
   `,
    methods: {
        regForm: function() {
            let self = this;
            let upform = document.getElementById("regisForm");
            let formData = new FormData(upform)
            
            fetch("/api/users/register", {
                method: "POST",
                body: formData,
                headers:{
                    'X-CSRFToken': token
                },
                
                credentials: 'same-origin'
                
            }).then(function(res){
                return res.json();
                
            }).then(function(l){
                self.msg = l;
                console.log(l);
                if(l.msg == "success"){
                    router.replace("/");
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    data: function() {
        return { msg:[] }
    }
});

const Login = Vue.component('login',{
    template: `
    <div class="login">
        <h1>Login</h1>
        <p>Login to your account</p>
        <hr>
        
        <form id="loginForm" @submit.prevent="Login" method="POST" enctype="multipart/form">
            <label for="username"><b>Username</b></label>
            <input type="text" placeholder="Enter username" name="username" required>
            
            <label for="psw"><b>Password</b></label>
            <input type="password" placeholder="Enter Password" name="psw" required>
            
            <button type=submit class="btn btn-primary"> Login </button>
        </form>
    </div>
   `,
    methods: {
        logForm: function() {
            let self = this;
            let upform = document.getElementById("loginForm");
            let formData = new FormData(upform)
            
            fetch("/api/auth/login", {
                method: "POST",
                body: formData,
                headers:{
                    'X-CSRFToken': token
                },
                credentials: 'same-origin'
            }).then(function(res){
                console.log(res);
                return res.json();
            }).then(function(r){
                console.log(r);
                self.msg = r;
                if(r.msg == "success"){
                    console.log("success recieved");
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    data: function() {
        return {}
    }
});

const Logout = Vue.component('logout',{
    template:`
    <div>
    </div>
    `,
    methods: {
        func: function(){
            fetch("/api/auth/logout",{
                method: "GET",
                credentials: 'same-origin'
            }).then(function(res){
                return res.json();
            }).then(function(a){
                if(a.status == "OK"){
                    router.replace("/");
                }
            }).catch(function(x){
                console.log(x);
            });
        }
    },
    mounted: function(){
        this.func();
    },
    data: function() {
        return {}
    }
});

const Explore = Vue.component('explore',{
    template: `
    <div class="viewAll">
        <h3>explore Place holder</h3>
        <div class="">
            <ul class="seePosts">
                <li class="vItems" style="visibility:hidden;">
                    <div class="info">
                        <p id="postername"></p>
                    </div>
                    <div class="getPic">
                        <img id="postImg" src="" alt="post image" />
                    </div>
                    <div class="capPic">
                        <p id="postCapt"></p>
                    </div>
                </li>
            </ul>
        </div>
    </div>
    `,
    methods: {
        func: function(){
            fetch("/api/posts",{
                method: "GET"
            }).then(function(res){
                return res.json();
            }).then(function(r){
                console.log(r);
                var l = document.getElementsByClassName("seePosts")[0];
                for(var x = 0; x < r.posts.length; x++){
                    var copy = document.getElementsByClassName("vItems")[0].cloneNode(true);
                    copy.style.visibility = "visible";
                    var n = copy.childNodes;
                    //console.log("n: "+n.length);
                    n[1].firstChild.src = "/static/posts/"+r.posts[x].image;
                    n[4].innerHTML = r.posts[x].caption;
                    l.appendChild(copy);
                }
            }).catch(function(er){
                console.log(er);
            });
        }
    },
    mounted: function(){
        this.func();
    },
    data: function() {
        return {}
    }
});

const NotFound = Vue.component('not-found', {
    template: `
    <div>
        <h1>404 - Not Found</h1>
    </div>
    `,
    data: function () {
        return {}
    }
});

const UserProfile = Vue.component('userProfile',{
    template: `
    <div class="userProf">
        <h3>Profile place holder</h3>
        <p id="userID" style="visibility:hidden;">{{ var1 }}</p>
        <div class="infoSect">
        </div>
        <div class="postSec">
        </div>
    </div>
    `,
    methods: {
        retr: function(){
            var a = document.getElementById("userID");
            fetch("/api/users/"+a.innerHTML+"/posts",{
                method: "GET"
            }).then(function(res){
                return res.json();
            }).then(function(p){
                console.log(p);
            }).catch(function(e){
                console.log(e);
            });
        }
    },
    mounted: function(){
        this.retr();
    },
    data: function() {
        return {
            var1: u_id
        }
    }
});

const AddPost = Vue.component('addPost',{
    template:`
    <div class="newPost">
        <h3>New Post</h3>
        <form id="pForm" @submit.prevent="postForm" method="POST" enctype="multipart/form-data">
            <div class="formSect">
                <label for="capt"> Caption:</label>
                <input type="text" name="capt" />
            </div>
            <div class="formSect">
                <label for="photo">Picture:</label>
                <input type="file" name="photo" />
            </div>
            <br />
            <button type="submit">Post</button>
        </form>
    </div>
    `,
    methods: {
        postForm: function() {
            let self = this;
            let upform = document.getElementById("pForm");
            let formData = new FormData(upform)
            
            fetch("/api/users/"+u_id+"/posts", {
                method: "POST",
                body: formData,
                headers:{
                    'X-CSRFToken': token
                },
                credentials: 'same-origin'
            }).then(function(res){
                console.log(res);
                return res.json();
            }).then(function(newp){
                console.log(newp);
                self.msg = newp;
                if(newp.msg == "success"){
                    console.log("success recieved");
                }
            }).catch(function(adding){
                console.log(adding);
            });
        }
    },
    data: function() {
        return {}
    }
});

// Define Routes
const router = new VueRouter({
    mode: 'history',
    routes: [
        {path: "/", component: Home},
        // Put other routes here
        {path: "/register", component: Register},
        {path: "/login", component: Login},
        {path: "/logout", component: Logout},
        {path: "/explore", component: Explore},
        {path: "/users/{user_id}", component: UserProfile},
        {path: "/posts/new", component: AddPost},
        // This is a catch all route in case none of the above matches
        {path: "*", component: NotFound}
    ]
});

// Instantiate our main Vue Instance
let app = new Vue({
    el: "#app",
    router
});