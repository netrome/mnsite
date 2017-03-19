/**
 * Created by marten on 2017-03-17.
 */

var comp = Vue.component('mn-list', {
    template: `
<div class="w3-third w3-panel w3-light-gray">
<ul class="w3-ul w3-card-4 w3-panel w3-white">
<li>
<i class="w3-btn w3-right w3-white fa fa-save" v-on:click="save_items()"></i>
<i class="w3-btn w3-right w3-white fa fa-remove" v-on:click="remove_list()"></i>
<h3 class="w3-center">{{ name }}</h3></li>
<li v-for="(value, key) in mn_items" :key="key">
<i class="w3-btn w3-right w3-white fa fa-close" v-on:click="remove_from_list(key)"></i>
<p v-on:click="toggle_item(key)"><del v-if="!value">{{ key }}</del><span v-else="">{{ key }}</span></p>
</li>
<li>{{ list_input }}</li>
<input type="text" class="w3-input w3-row" v-model="list_input" v-on:keyup.enter="add_to_list(list_input)" placeholder="Add item...">
</ul>
</div>
`,
    data: function () {
        return {
            mn_items: {}, //{Bananas: true, Eggs: false, Spam: true},
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
            for (val in this.mn_items){
                if (val != value){
                    new_stuff[val] = this.mn_items[val];
                }
            }

            this.mn_items = new_stuff;

        },

        toggle_item: function (item) {
            Vue.set(this.mn_items, item, !this.mn_items[item])
        },

        save_items: function () {
            // Send ajax data to server
            var data = $.extend({mn_name: this.name} ,this.mn_items);

            $.post("/list/save/" + this.pk, data);
            if (this.pk == "0"){
                location.reload();
            }
        },

        remove_list: function () {
            // Send remove request
            $.post("/list/remove/" + this.pk, {});
            location.reload();
        }
    },

    mounted: function () {
        var self = this;

        $.get("/list/items/" + this.pk, function (data, status) {
            var the_items = {};
            data = JSON.parse(data);
            for (var index in data){
                var the_item = data[index].fields;
                var name = the_item.name;
                var status = the_item.active;
                the_items[name] = status;
            }
            self.mn_items = the_items;
        });
    },

    props: {
        name: String,
        pk: String,
    }
});

var app = new Vue({
    el: "#app",
    data: {
        new_list_name: "",
    },
    methods: {
        new_list: function () {
            alert("Ny lista");
        }
    }
});

/*
function get_list_items(list_pk) {
    var the_items = {};
    $.get("/list/items/" + list_pk, function (data, status) {
        alert("Data: " + data);
        data = JSON.parse(data);
        for (var index in data){
            var the_item = data[index].fields;
            var name = the_item.name;
            var status = the_item.active;
            the_items[name] = status;
        }
    });
    return the_items;
}
*/