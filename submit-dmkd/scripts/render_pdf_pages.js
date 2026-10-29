ObjC.import('AppKit'); ObjC.import('PDFKit'); ObjC.import('Foundation');
function run(argv) {
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  var n = doc.pageCount; var scale = parseFloat(argv[2] || '1.5');
  for (var i = 0; i < n; i++) {
    var page = doc.pageAtIndex(i);
    var b = page.boundsForBox($.kPDFDisplayBoxMediaBox);
    var w = Math.round(b.size.width * scale), h = Math.round(b.size.height * scale);
    var rep = $.NSBitmapImageRep.alloc.initWithBitmapDataPlanesPixelsWidePixelsHighBitsPerSampleSamplesPerPixelHasAlphaIsPlanarColorSpaceNameBytesPerRowBitsPerPixel(null, w, h, 8, 4, true, false, $.NSDeviceRGBColorSpace, 0, 0);
    var ctx = $.NSGraphicsContext.graphicsContextWithBitmapImageRep(rep);
    $.NSGraphicsContext.saveGraphicsState; $.NSGraphicsContext.setCurrentContext(ctx);
    $.NSColor.whiteColor.setFill; $.NSRectFill($.NSMakeRect(0, 0, w, h));
    var t = $.NSAffineTransform.transform; t.scaleBy(scale); t.concat;
    page.drawWithBoxToContext($.kPDFDisplayBoxMediaBox, ctx.CGContext);
    $.NSGraphicsContext.restoreGraphicsState;
    var data = rep.representationUsingTypeProperties($.NSBitmapImageFileTypePNG, $());
    var name = argv[1] + '/p' + (i < 9 ? '0' : '') + (i + 1) + '.png';
    data.writeToFileAtomically(name, true);
  }
  return 'pages ' + n;
}
