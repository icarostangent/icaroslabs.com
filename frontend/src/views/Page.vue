<template>
  <div class="col-md-8 mx-auto page">
    <div>
      <h1>{{ this.page.title.rendered }}</h1>
    </div>
    <div v-html="page.content.rendered"></div>
  </div>
</template>

<script>

export default {
  name: "Page",
  components: {
  },
  computed: {
    page() {
      return this.$store.state.page[0];
    },
  },
  mounted() {
    console.log(this.page);
    this.$store.dispatch("getPage", { slug: this.$route.params.slug });
  },
};
</script>
