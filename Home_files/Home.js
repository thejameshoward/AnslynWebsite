// Created by iWeb 3.0.1 local-build-20170309

setTransparentGifURL('Media/transparent.gif');function applyEffects()
{var registry=IWCreateEffectRegistry();registry.registerEffects({stroke_0:new IWStrokeParts([{rect:new IWRect(-5,5,10,515),url:'Home_files/stroke.png'},{rect:new IWRect(-5,-5,10,10),url:'Home_files/stroke_1.png'},{rect:new IWRect(5,-5,776,10),url:'Home_files/stroke_2.png'},{rect:new IWRect(781,-5,11,10),url:'Home_files/stroke_3.png'},{rect:new IWRect(781,5,11,515),url:'Home_files/stroke_4.png'},{rect:new IWRect(781,520,11,10),url:'Home_files/stroke_5.png'},{rect:new IWRect(5,520,776,10),url:'Home_files/stroke_6.png'},{rect:new IWRect(-5,520,10,10),url:'Home_files/stroke_7.png'}],new IWSize(786,525))});registry.applyEffects();}
function hostedOnDM()
{return false;}
function onPageLoad()
{loadMozillaCSS('Home_files/HomeMoz.css')
adjustLineHeightIfTooBig('id1');adjustFontSizeIfTooBig('id1');Widget.onload();fixupAllIEPNGBGs();fixAllIEPNGs('Media/transparent.gif');applyEffects()}
function onPageUnload()
{Widget.onunload();}
