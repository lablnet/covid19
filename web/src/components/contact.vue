<template>
<form class="container" action="https://formspree.io/f/xzbvkrwy" method="POST">
    <div class="form-group mt-2">
        <label class="content">Name:</label>
        <input name="name" id="name" type="text" class="form-control" required />
    </div>
    <div class="form-group mt-2">
        <label class="content">Email:</label>
        <input name="_replyto" id="email" type="email" class="form-control" required />
    </div>
    <div class="form-group mt-2">
          <label class="content">Msg:</label>
        <textarea cols="5" rows="5" class="form-control" id="message" name="message" required></textarea>
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
