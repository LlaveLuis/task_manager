$(function()
{
   function active_item()
   {
      $("li.li-menu").removeClass('active');
      $("li.li-submenu").removeClass('active');
      $item = $(this).parents("li.li-menu");
      $item.addClass('active');
   }
   $("li.li-menu:not(.dropdown) a").on('click', active_item);
   $("li.li-submenu a").on('click', active_item);
});