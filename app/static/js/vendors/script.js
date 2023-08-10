
/* django product form

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=QuillWidget(attrs={'class': 'form-control ', 'placeholder': 'Description'}), required=False)
    class Meta:
        
        model = Product
        fields = ['name','category', 'weigth', 'units','images','price','sale_price','description','meta_title','meta_description','status','in_stock','code','sku']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'weigth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weight'}),
            'units': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Units'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$0'}),
            'sale_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$0'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meta Title'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'status': forms.Select(attrs={'class': 'form-control , form-check-input , form-check form-check-inline', 'placeholder': 'Status'}),
            'in_stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'In Stock'}),
            'description': forms.CharField(widget=QuillWidget(attrs={'class': 'form-control' , 'placeholder': 'Description' })),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'images' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Images'}),

        }






*/

/* 


Quickview structure  html 


<div class="modal fade" id="quickViewModal" tabindex="-1" aria-hidden="true">
   <div class="modal-dialog modal-xl modal-dialog-centered">
      <div class="modal-content">
         <div class="modal-body p-8">
            <div class="position-absolute top-0 end-0 me-3 mt-3">
               <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="row">
               <div class="col-lg-6">
                  <!-- img slide -->
                  <div class="product productModal" id="productModal">

                  </div>
                  <!-- product tools -->
                  <div class="product-tools">
                     <div class="thumbnails row g-3" id="productModalThumbnails">
                        <div class="col-3" class="tns-nav-active">
                           <div class="thumbnails-img">
                              <!-- img -->
                              <img src="../../static/images/products/product-single-img-1.jpg" alt="">
                           </div>
                        </div>



                     </div>
                  </div>
               </div>
               <div class="col-lg-6">
                  <div class="ps-lg-8 mt-6 mt-lg-0">
                     <a href="#!" class="mb-4 d-block">Bakery Biscuits</a>
                     <h2 class="mb-1 h1">Napolitanke Ljesnjak</h2>
                     <div class="mb-4">
                        <small class="text-warning">
                           <i class="bi bi-star-fill"></i>
                           <i class="bi bi-star-fill"></i>
                           <i class="bi bi-star-fill"></i>
                           <i class="bi bi-star-fill"></i>
                           <i class="bi bi-star-half"></i></small><a href="#" class="ms-2">(30 reviews)</a>
                     </div>
                     <div class="fs-4">
                        <span class="fw-bold text-dark">$32</span>
                        <span class="text-decoration-line-through text-muted">$35</span><span><small
                              class="fs-6 ms-2 text-danger">26% Off</small></span>
                     </div>
                     <hr class="my-6">
                     <div class="mb-4">
                        <button type="button" class="btn btn-outline-secondary">
                           250g
                        </button>
                        <button type="button" class="btn btn-outline-secondary">
                           500g
                        </button>
                        <button type="button" class="btn btn-outline-secondary">
                           1kg
                        </button>
                     </div>
                     <div>
                        <!-- input -->
                        <!-- input -->
                        <div class="input-group input-spinner  ">
                           <input type="button" value="-" class="button-minus  btn  btn-sm " data-field="quantity">
                           <input type="number" step="1" max="10" value="1" name="quantity"
                              class="quantity-field form-control-sm form-input   ">
                           <input type="button" value="+" class="button-plus btn btn-sm " data-field="quantity">
                        </div>
                     </div>
                     <div class="mt-3 row justify-content-start g-2 align-items-center">

                        <div class="col-lg-4 col-md-5 col-6 d-grid">
                           <!-- button -->
                           <!-- btn -->
                           <button type="button" class="btn btn-primary">
                              <i class="feather-icon icon-shopping-bag me-2"></i>Add to
                              cart
                           </button>
                        </div>
                        <div class="col-md-4 col-5">
                           <!-- btn -->
                           <a class="btn btn-light" href="#" data-bs-toggle="tooltip" data-bs-html="true"
                              aria-label="Compare"><i class="bi bi-arrow-left-right"></i></a>
                           <a class="btn btn-light" href="#!" data-bs-toggle="tooltip" data-bs-html="true"
                              aria-label="Wishlist"><i class="feather-icon icon-heart"></i></a>
                        </div>
                     </div>
                     <hr class="my-6">
                     <div>
                        <table class="table table-borderless">
                           <tbody>
                              <tr>
                                 <td>Product Code:</td>
                                 <td>FBB00255</td>
                              </tr>
                              <tr>
                                 <td>Availability:</td>
                                 <td>In Stock</td>
                              </tr>
                              <tr>
                                 <td>Category:</td>
                                 <td>Fruits</td>
                              </tr>
                              <tr>
                                 <td>Shipping:</td>
                                 <td>
                                    <small>01 day shipping.<span class="text-muted">( Free pickup today)</span></small>
                                 </td>
                              </tr>
                           </tbody>
                        </table>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</div>


*/

// quickview
   $(document).ready(function () {
      $('.btn-action').click(function () {
         var productId = $(this).data('product-id');
         $.ajax({
            type: 'GET',
            url: '/quick_view/' + productId + '/',
            data: {
               'product_id': productId
            },
            success: function (data) {
               $('#quickViewModal .modal-body .productModal').html(`
                  <div class="zoom" onmousemove="zoom(event)" style="background-image: url(${data.images});">
                     <img src="${data.images}" alt="">
                  </div>
               `);

               var thumbnails = '';
               $.each(data.thumbnail_images, function (index, thumbnail) {
                  thumbnails += `
                     <div class="col-3 ${index === 0 ? 'tns-nav-active' : ''}">
                        <div class="thumbnails-img">
                           <img src="${thumbnail}" alt="">
                        </div>
                     </div>
                  `;
               });
               $('#quickViewModal .modal-body .product-tools .thumbnails').html(thumbnails);
              /* quickview <div class="ps-lg-8 mt-6 mt-lg-0">
                     <a href="#!" class="mb-4 d-block">Bakery Biscuits</a> */
               $('#quickViewModal .modal-body .ps-lg-8.mt-6.mt-lg-0 a.mb-4.d-block').attr('href', data.product_url);
               $('#quickViewModal .modal-body .mb-4.d-block').attr('href', data.product_url);
               $('#quickViewModal .modal-body .h1').text(data.name);
               $('#quickViewModal .modal-body .text-warning').html(data.rating_stars);
               $('#quickViewModal .modal-body .fs-4 .text-dark').text(data.price);
               $('#quickViewModal .modal-body .text-decoration-line-through').text(data.sale_price);
               $('#quickViewModal .modal-body .fs-6.text-danger').text(data.discount);
               /* in_sotck */
               $('#quickViewModal .modal-body .table.table-borderless tbody tr:nth-child(2) td:nth-child(2)').text(data.in_stock);
               /* product_code */
               $('#quickViewModal .modal-body .table.table-borderless tbody tr:nth-child(1) td:nth-child(2)').text(data.code);
               /* category */
               $('#quickViewModal .modal-body .table.table-borderless tbody tr:nth-child(3) td:nth-child(2)').text(data.category);
               var category_link = document.getElementById('category_link');
            category_link.href = data.category_url;
            category_link.innerHTML = data.category;
               
               var quantityButtons = `
                  <div class="input-group input-spinner">
                     <input type="button" value="-" class="button-minus btn btn-sm" data-field="quantity">
                     <input type="number" step="1" max="10" value="1" name="quantity" class="quantity-field form-control-sm form-input">
                     <input type="button" value="+" class="button-plus btn btn-sm" data-field="quantity">
                  </div>
               `;
               $('#quickViewModal .modal-body .input-group.input-spinner').replaceWith(quantityButtons);

               $('#quickViewModal .modal-body .col-lg-4.col-md-5.col-6.d-grid button.btn-primary').attr('data-product-id', data.id);
               

            },
            error: function (xhr, status, error) {
               console.error(error);
            }
         });
      });
   });

/* getelementbyid  <a> by id category_link and replace value with url */

/* new script how replicate quickview html structure and show the data from form */
