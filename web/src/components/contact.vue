<template>
<form class="container">
    <div class="form-group mt-2">
        <label class="content">Name:</label>
        <input name="name" id="name" type="text" class="form-control" />
    </div>
    <div class="form-group mt-2">
        <label class="content">Email:</label>
        <input name="name" id="name" type="text" class="form-control" />
    </div>
    <div class="form-group mt-2">
        <label class="content">Msg:</label>
        <textarea cols="5" rows="5" class="form-control"></textarea>
    </div>
    <div class="form-group mt-2 mb-3">
        <input type="submit" value="Submit" class="btn btn-primary" />
    </div>
</form>
</template>

<script lang="js">
export default {
  name: "contact",
  mounted() {
    window.scrollTo(0, 0)
  }
}
</script>