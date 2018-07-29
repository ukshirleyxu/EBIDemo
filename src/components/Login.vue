<template>
  <div class="login">
    <div>
      <h1>Insert</h1>
      <Input v-model="insertValue" placeholder="Insert to database" clearable style="width: 200px"></Input>
    	<Button @click="insert">Insert</Button>
      <div><span v-for="item in insertResults">{{item.name}};</span></div>
      
    </div>
    <div>
      <h1>Search by MongoDB</h1>
      <Input v-model="searchValue" placeholder="Search from database" clearable style="width: 200px"></Input>
      <Button @click="searchMongo">Search</Button>
      <div><span v-for="item in searchResults">{{item.name}};</span></div>
    </div>
    <div>
      <h1>Search by Solr</h1>
      <Input v-model="solrValue" placeholder="Search from database" clearable style="width: 200px"></Input>
      <Button @click="searchSolr">Search</Button>
      <div><span v-for="item in solrResults">{{item.name}}:{{item.age}};</span></div>
    </div>
  </div>

</template>


<script>
export default {
  name: 'HelloWorldShilrey123',
  data () {
    return {
      insertValue:'',
      searchValue:'',
      solrValue:'',
      insertResults:[],
      searchResults:[],
      solrResults:[] 
    }
  },
  methods:{
    insert(){
      this.$http
            .post('/api/insert',{data:this.insertValue,age: parseInt(Math.random()*100)})
            .then(function(res){
              console.log(res.body);
              this.insertResults = res.body.res;
            },function(err){

            });
    },
    searchMongo(){
      this.$http
            .get('/api/searchmongo?data='+this.searchValue)
            .then(function(res){
              console.log(res.body)
              this.searchResults = res.body.res;
              if(this.searchResults.length == 0)
                alert('No resutls');
            },function(err){

            });
    },
    searchSolr(){
      this.$http
            .get('/api/searchsolr?age='+this.solrValue)
            .then(function(res){
              console.log(res.body)
              this.solrResults = res.body.res;
              if(this.solrResults.length == 0)
                alert('No resutls');
            },function(err){

            });
    }
  },
  mounted(){
  	
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .login{
    text-align: center;
  }
</style>
