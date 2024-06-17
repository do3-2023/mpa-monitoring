<script lang="ts">
import { addNewPerson } from '../database/person';

export default {
    name: "AddPerson",
    data() {
      return {
        last_name: "",
        phone_number: "",
        location: ""
      }
    },
    methods: {
      async addPerson() {
        let person = {
          last_name: this.last_name,
          phone_number: this.phone_number,
          location: this.location
        }
        addNewPerson(person)
        this.last_name = ""
        this.phone_number = ""
        this.location = ""
      }
    }
}
</script>

<template>
  <h1>Add a new person</h1>
  <router-link :to="{ name: 'home'}">
    <button>Return to homepage</button>
  </router-link>

<form v-on:submit.prevent="addPerson">
  <p>Last name: <input type="text" required v-model="last_name"></p>
  <p>Phone number: <input type="text" required v-model="phone_number"></p>
  <p>Location: <input type="text" required v-model="location"></p>
  <button type="submit" @click="addPerson">Submit</button>
</form>

</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
