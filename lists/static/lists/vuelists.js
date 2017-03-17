/**
 * Created by marten on 2017-03-17.
 */

Vue.component('mn-list', {
    template: `
<div class="w3-third w3-panel w3-light-gray">
<ul class="w3-ul w3-card-4 w3-panel w3-white">
<li><h3 class="w3-center">{{ name }}</h3></li>
<li v-for="(value, key) in mn_items" :key="key">
<i class="w3-btn w3-right w3-white fa-close" v-on:click="remove_from_list(key)"></i>
<p v-on:click="toggle_item(key)"><del v-if="!value">{{ key }}</del><span v-else="">{{ key }}</span></p>
</li>
<li>{{ list_input }}</li>
<input type="text" class="w3-input w3-row" v-model="list_input" v-on:keyup.enter="add_to_list(list_input)" placeholder="Add item...">
</ul>
</div>
`,
    data: function () {
        return {
            mn_items: {Bananas: true, Eggs: false, Spam: true},
            list_input: ""
        }
    },

    methods: {
        add_to_list: function (value) {
            Vue.set(this.mn_items, value, true);
            this.list_input = "";
        },

        remove_from_list: function (value) {
            // Ugly code now
            var new_stuff = {};
            for (key in this.mn_items){
                if (key != value){
                    new_stuff[key] = this.mn_items[key];
                }
            }

            this.mn_items = new_stuff;

        },

        toggle_item: function (item) {
            Vue.set(this.mn_items, item, !this.mn_items[item])
        },
    },

    props: {
        name: String
    }
});

new Vue({
    el: "#app",
});
