/** @odoo-module*/

odoo.define("latest_events.dynamic", function (require) {
  "use strict";
  console.log("start");
  var publicWidget = require("web.public.widget");
  var ajax = require("web.ajax");
  console.log("running");
  var Dynamic = publicWidget.Widget.extend({
    selector: ".events_dynamic",
    start: function () {
      var self = this;
      ajax.jsonRpc("/events/snippet", "call", {}).then(function (result) {
                self.$target.empty().append(result);
           });
        console.log("worked");
    },
  });

  publicWidget.registry.latest_events = Dynamic;
  console.log("end");
  return Dynamic;
});
Footer
