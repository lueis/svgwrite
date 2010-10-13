#coding:utf-8

from types import SVGAttribute, SVGMultiAttribute

empty_list = []

tiny12_attributes = {
'about': SVGAttribute('about', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'accent-height': SVGAttribute('accent-height', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'accumulate': SVGAttribute('accumulate', anim=False,
    types=empty_list,
    const=frozenset([u'none', u'sum'])),
'additive': SVGAttribute('additive', anim=False,
    types=empty_list,
    const=frozenset([u'replace', u'sum'])),
'alphabetic': SVGAttribute('alphabetic', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'arabic-form': SVGAttribute('arabic-form', anim=False,
    types=empty_list,
    const=frozenset([u'terminal', u'initial', u'isolated', u'medial'])),
'ascent': SVGAttribute('ascent', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'attributeName': SVGAttribute('attributeName', anim=False,
    types=frozenset([u'name']),
    const=empty_list),
'attributeType': SVGAttribute('attributeType', anim=False,
    types=empty_list,
    const=frozenset([u'XML', u'CSS', u'auto'])),
'audio-level': SVGAttribute('audio-level', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'bandwidth': SVGAttribute('bandwidth', anim=False,
    types=frozenset([u'number']),
    const=frozenset([u'auto'])),
'baseProfile': SVGAttribute('baseProfile', anim=False,
    types=empty_list,
    const=frozenset([u'none', u'tiny', u'basic', u'full'])),
'bbox': SVGAttribute('bbox', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'begin': SVGAttribute('begin', anim=False,
    types=frozenset([u'list-of-string']),
    const=empty_list),
'buffered-rendering': SVGAttribute('buffered-rendering', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'dynamic', u'static', u'inherit'])),
'by': SVGAttribute('by', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'calcMode': SVGAttribute('calcMode', anim=False,
    types=empty_list,
    const=frozenset([u'discrete', u'linear', u'paced', u'spline'])),
'cap-height': SVGAttribute('cap-height', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'class': SVGAttribute('class', anim=True,
    types=frozenset([u'XML-Name']),
    const=empty_list),
'color': SVGAttribute('color', anim=True,
    types=frozenset([u'color']),
    const=frozenset([u'inherit'])),
'color-rendering': SVGAttribute('color-rendering', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'optimizeSpeed', u'optimizeQuality', u'inherit'])),
'content': SVGAttribute('content', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'contentScriptType': SVGAttribute('contentScriptType', anim=False,
    types=frozenset([u'anything']),
    const=empty_list),
'cx': SVGAttribute('cx', anim=True,
    types=frozenset([u'coordinate']),
    const=empty_list),
'cy': SVGAttribute('cy', anim=True,
    types=frozenset([u'coordinate']),
    const=empty_list),
'd': SVGAttribute('d', anim=True,
    types=frozenset([u'path-data']),
    const=empty_list),
'datatype': SVGAttribute('datatype', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'defaultAction': SVGAttribute('defaultAction', anim=False,
    types=empty_list,
    const=frozenset([u'perform', u'cancel'])),
'descent': SVGAttribute('descent', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'direction': SVGAttribute('direction', anim=False,
    types=empty_list,
    const=frozenset([u'ltr', u'rtl', u'inherit'])),
'display': SVGAttribute('display', anim=True,
    types=empty_list,
    const=frozenset([u'inline', u'block', u'list-item', u'run-in', u'compact',
                     u'marker', u'table', u'inline-table', u'table-row-group',
                     u'table-header-group', u'table-footer-group', u'table-row',
                     u'table-column-group', u'table-column', u'table-cell',
                     u'table-caption', u'none', u'inherit'])),
'display-align': SVGAttribute('display-align', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'before', u'center', u'after', u'inherit'])),
'dur': SVGAttribute('dur', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'media', u'indefinite'])),
'editable': SVGAttribute('editable', anim=True,
    types=empty_list,
    const=frozenset([u'none', u'simple'])),
'end': SVGAttribute('end', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'ev:event': SVGAttribute('ev:event', anim=False,
    types=frozenset([u'XML-Name']),
    const=empty_list),
'event': SVGAttribute('event', anim=False,
    types=frozenset([u'XML-Name']),
    const=empty_list),
'externalResourcesRequired': SVGAttribute('externalResourcesRequired', anim=False,
    types=frozenset([u'boolean']),
    const=empty_list),
'fill': SVGAttribute('fill', anim=True,
    types=frozenset([u'paint']),
    const=frozenset([u'inherit'])),
'fill-opacity': SVGAttribute('fill-opacity', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'fill-rule': SVGAttribute('fill-rule', anim=True,
    types=empty_list,
    const=frozenset([u'nonzero', u'evenodd', u'inherit'])),
'focusHighlight': SVGAttribute('focusHighlight', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'none'])),
'focusable': SVGAttribute('focusable', anim=True,
    types=frozenset([u'boolean']),
    const=frozenset([u'auto'])),
'font-family': SVGAttribute('font-family', anim=True,
    types=frozenset([u'string']),
    const=frozenset([u'inherit'])),
'font-size': SVGAttribute('font-size', anim=True,
    types=frozenset([u'length']),
    const=frozenset([u'inherit'])),
'font-stretch': SVGAttribute('font-stretch', anim=False,
    types=empty_list,
    const=frozenset([u'condensed', u'normal', u'ultra-condensed', u'expanded',
                     u'narrower', u'inherit', u'semi-condensed', u'extra-condensed',
                     u'ultra-expanded', u'wider', u'semi-expanded', u'extra-expanded'])),
'font-style': SVGAttribute('font-style', anim=True,
    types=empty_list,
    const=frozenset([u'normal', u'italic', u'oblique', u'inherit'])),
'font-variant': SVGAttribute('font-variant', anim=True,
    types=empty_list,
    const=frozenset([u'normal', u'small-caps', u'inherit'])),
'font-weight': SVGAttribute('font-weight', anim=True,
    types=empty_list,
    const=frozenset([u'normal', u'bold', u'bolder', u'lighter', u'100', u'200',
                     u'300', u'400', u'500', u'600', u'700', u'800', u'900',
                     u'inherit'])),
'from': SVGAttribute('from', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'g1': SVGAttribute('g1', anim=False,
    types=frozenset([u'list-of-name']),
    const=empty_list),
'g2': SVGAttribute('g2', anim=False,
    types=frozenset([u'list-of-name']),
    const=empty_list),
'glyph-name': SVGAttribute('glyph-name', anim=False,
    types=frozenset([u'list-of-name']),
    const=empty_list),
'gradientUnits': SVGAttribute('gradientUnits', anim=True,
    types=empty_list,
    const=frozenset([u'userSpaceOnUse', u'objectBoundingBox'])),
'handler': SVGAttribute('handler', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'hanging': SVGAttribute('hanging', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'height': SVGMultiAttribute({
    '*': SVGAttribute(
        'height', anim=True,
        types=frozenset([u'length']),
        const=empty_list),
    'textArea': SVGAttribute(
        'height', anim=True,
        types=frozenset([u'length']),
        const=frozenset([u'auto'])),
    }),
'horiz-adv-x': SVGAttribute('horiz-adv-x', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'horiz-origin-x': SVGAttribute('horiz-origin-x', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'id': SVGAttribute('id', anim=False,
    types=frozenset([u'name']),
    const=empty_list),
'ideographic': SVGAttribute('ideographic', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'image-rendering': SVGAttribute('image-rendering', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'optimizeSpeed', u'optimizeQuality', u'inherit'])),
'initialVisibility': SVGAttribute('initialVisibility', anim=False,
    types=empty_list,
    const=frozenset([u'whenStarted', u'always'])),
'k': SVGAttribute('k', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'keyPoints': SVGAttribute('keyPoints', anim=False,
    types=frozenset([u'semicolon-list']),
    const=empty_list),
'keySplines': SVGAttribute('keySplines', anim=False,
    types=frozenset([u'semicolon-list']),
    const=empty_list),
'keyTimes': SVGAttribute('keyTimes', anim=False,
    types=frozenset([u'semicolon-list']),
    const=empty_list),
'lang': SVGAttribute('lang', anim=False,
    types=frozenset([u'list-of-name']),
    const=empty_list),
'line-increment': SVGAttribute('line-increment', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'auto', u'inherit'])),
'mathematical': SVGAttribute('mathematical', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'max': SVGAttribute('max', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'media'])),
'mediaCharacterEncoding': SVGAttribute('mediaCharacterEncoding', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'mediaContentEncodings': SVGAttribute('mediaContentEncodings', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'mediaSize': SVGAttribute('mediaSize', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'mediaTime': SVGAttribute('mediaTime', anim=False,
    types=frozenset([u'time']),
    const=empty_list),
'min': SVGAttribute('min', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'media'])),
'nav-down': SVGAttribute('nav-down', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-down-left': SVGAttribute('nav-down-left', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-down-right': SVGAttribute('nav-down-right', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-left': SVGAttribute('nav-left', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-next': SVGAttribute('nav-next', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-prev': SVGAttribute('nav-prev', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-right': SVGAttribute('nav-right', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-up': SVGAttribute('nav-up', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-up-left': SVGAttribute('nav-up-left', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'nav-up-right': SVGAttribute('nav-up-right', anim=True,
    types=frozenset([u'focus']),
    const=empty_list),
'observer': SVGAttribute('observer', anim=False,
    types=frozenset([u'IDREF']),
    const=empty_list),
'offset': SVGAttribute('offset', anim=True,
    types=frozenset([u'number']),
    const=empty_list),
'opacity': SVGAttribute('opacity', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'origin': SVGAttribute('origin', anim=False,
    types=empty_list,
    const=frozenset([u'default'])),
'overlay': SVGAttribute('overlay', anim=False,
    types=empty_list,
    const=frozenset([u'none', u'top'])),
'overline-position': SVGAttribute('overline-position', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'overline-thickness': SVGAttribute('overline-thickness', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'panose-1': SVGAttribute('panose-1', anim=False,
    types=frozenset([u'list-of-integer']),
    const=empty_list),
'path': SVGAttribute('path', anim=False,
    types=frozenset([u'list-of-name']),
    const=empty_list),
'pathLength': SVGAttribute('pathLength', anim=True,
    types=frozenset([u'number']),
    const=empty_list),
'phase': SVGAttribute('phase', anim=False,
    types=empty_list,
    const=frozenset([u'default', u'capture'])),
'playbackOrder': SVGAttribute('playbackOrder', anim=False,
    types=empty_list,
    const=frozenset([u'all', u'forwardOnly'])),
'pointer-events': SVGAttribute('pointer-events', anim=True,
    types=empty_list,
    const=frozenset([u'visiblePainted', u'visibleFill', u'visibleStroke', u'visible',
                     u'painted', u'fill', u'stroke', u'all', u'none', u'inherit'])),
'points': SVGAttribute('points', anim=True,
    types=frozenset([u'list-of-number']),
    const=empty_list),
'preserveAspectRatio': SVGAttribute('preserveAspectRatio', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'propagate': SVGAttribute('propagate', anim=False,
    types=empty_list,
    const=frozenset([u'continue', u'stop'])),
'property': SVGAttribute('property', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'r': SVGAttribute('r', anim=True,
    types=frozenset([u'length']),
    const=empty_list),
'rel': SVGAttribute('rel', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'repeatCount': SVGAttribute('repeatCount', anim=False,
    types=frozenset([u'number']),
    const=frozenset([u'indefinite'])),
'repeatDur': SVGAttribute('repeatDur', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'indefinite'])),
'requiredExtensions': SVGAttribute('requiredExtensions', anim=False,
    types=frozenset([u'list-of-IRI']),
    const=empty_list),
'requiredFeatures': SVGAttribute('requiredFeatures', anim=False,
    types=frozenset([u'list-of-IRI']),
    const=empty_list),
'requiredFonts': SVGAttribute('requiredFonts', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'requiredFormats': SVGAttribute('requiredFormats', anim=False,
    types=frozenset([u'anything']),
    const=empty_list),
'resource': SVGAttribute('resource', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'restart': SVGAttribute('restart', anim=False,
    types=empty_list,
    const=frozenset([u'always', u'never', u'whenNotActive'])),
'rev': SVGAttribute('rev', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'role': SVGAttribute('role', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'rotate': SVGAttribute('rotate', anim=True,
    types=frozenset([u'list-of-number']),
    const=empty_list),
'rx': SVGAttribute('rx', anim=True,
    types=frozenset([u'length']),
    const=empty_list),
'ry': SVGAttribute('ry', anim=True,
    types=frozenset([u'length']),
    const=empty_list),
'shape-rendering': SVGAttribute('shape-rendering', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'optimizeSpeed', u'crispEdges', u'geometricPrecision', u'inherit'])),
'slope': SVGAttribute('slope', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'snapshotTime': SVGAttribute('snapshotTime', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'none'])),
'solid-color': SVGAttribute('solid-color', anim=True,
    types=frozenset([u'color']),
    const=frozenset([u'inherit'])),
'solid-opacity': SVGAttribute('solid-opacity', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'stemh': SVGAttribute('stemh', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'stemv': SVGAttribute('stemv', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'stop-color': SVGAttribute('stop-color', anim=True,
    types=frozenset([u'color']),
    const=frozenset([u'inherit'])),
'stop-opacity': SVGAttribute('stop-opacity', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'strikethrough-position': SVGAttribute('strikethrough-position', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'strikethrough-thickness': SVGAttribute('strikethrough-thickness', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'stroke': SVGAttribute('stroke', anim=True,
    types=frozenset([u'paint']),
    const=frozenset([u'inherit'])),
'stroke-dasharray': SVGAttribute('stroke-dasharray', anim=True,
    types=frozenset([u'list-of-length']),
    const=frozenset([u'none', u'inherit'])),
'stroke-dashoffset': SVGAttribute('stroke-dashoffset', anim=True,
    types=frozenset([u'length']),
    const=frozenset([u'inherit'])),
'stroke-linecap': SVGAttribute('stroke-linecap', anim=True,
    types=empty_list,
    const=frozenset([u'butt', u'round', u'square', u'inherit'])),
'stroke-linejoin': SVGAttribute('stroke-linejoin', anim=True,
    types=empty_list,
    const=frozenset([u'miter', u'round', u'bevel', u'inherit'])),
'stroke-miterlimit': SVGAttribute('stroke-miterlimit', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'stroke-opacity': SVGAttribute('stroke-opacity', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'stroke-width': SVGAttribute('stroke-width', anim=True,
    types=frozenset([u'length']),
    const=frozenset([u'inherit'])),
'syncBehavior': SVGAttribute('syncBehavior', anim=False,
    types=empty_list,
    const=frozenset([u'canSlip', u'locked', u'independent', u'default'])),
'syncBehaviorDefault': SVGAttribute('syncBehaviorDefault', anim=False,
    types=empty_list,
    const=frozenset([u'canSlip', u'locked', u'independent', u'inherit'])),
'syncMaster': SVGAttribute('syncMaster', anim=False,
    types=frozenset([u'boolean']),
    const=empty_list),
'syncTolerance': SVGAttribute('syncTolerance', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'default'])),
'syncToleranceDefault': SVGAttribute('syncToleranceDefault', anim=False,
    types=frozenset([u'time']),
    const=frozenset([u'inherit'])),
'systemLanguage': SVGAttribute('systemLanguage', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'target': SVGMultiAttribute({
    '* a': SVGAttribute(
        'target', anim=True,
        types=frozenset([u'XML-Name']),
        const=frozenset([u'_replace', u'_self', u'_parent', u'_top', u'_blank'])),
    'listener': SVGAttribute(
        'target', anim=False,
        types=frozenset([u'XML-Name']),
        const=empty_list),
    }),
'text-align': SVGAttribute('text-align', anim=True,
    types=empty_list,
    const=frozenset([u'start', u'center', u'end', u'inherit'])),
'text-anchor': SVGAttribute('text-anchor', anim=True,
    types=empty_list,
    const=frozenset([u'start', u'middle', u'end', u'inherit'])),
'text-rendering': SVGAttribute('text-rendering', anim=True,
    types=empty_list,
    const=frozenset([u'auto', u'optimizeSpeed', u'optimizeLegibility', u'geometricPrecision', u'inherit'])),
'timelineBegin': SVGAttribute('timelineBegin', anim=False,
    types=empty_list,
    const=frozenset([u'onLoad', u'onStart'])),
'to': SVGAttribute('to', anim=False,
    types=frozenset([u'time']),
    const=empty_list),
'transform': SVGAttribute('transform', anim=True,
    types=frozenset([u'transform-list']),
    const=frozenset([u'none'])),
'transformBehavior': SVGAttribute('transformBehavior', anim=False,
    types=empty_list,
    const=frozenset([u'geometric', u'pinned', u'pinned90', u'pinned180', u'pinned270'])),
'type': SVGMultiAttribute({
    '* audio image video': SVGAttribute(
        'type', anim=True,
        types=frozenset([u'content-type']),
        const=empty_list),
    'handler script': SVGAttribute(
        'type', anim=False,
        types=frozenset([u'content-type']),
        const=empty_list),
    'animateTransform': SVGAttribute(
        'type', anim=False,
        types=empty_list,
        const=frozenset([u'translate', u'scale', u'rotate', u'skewX', u'skewY'])),
    }),
'typeof': SVGAttribute('typeof', anim=True,
    types=frozenset([u'string']),
    const=empty_list),
'u1': SVGAttribute('u1', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'u2': SVGAttribute('u2', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'underline-position': SVGAttribute('underline-position', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'underline-thickness': SVGAttribute('underline-thickness', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'unicode': SVGAttribute('unicode', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'unicode-bidi': SVGAttribute('unicode-bidi', anim=False,
    types=empty_list,
    const=frozenset([u'normal', u'embed', u'bidi-override', u'inherit'])),
'unicode-range': SVGAttribute('unicode-range', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'units-per-em': SVGAttribute('units-per-em', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'values': SVGAttribute('values', anim=False,
    types=frozenset([u'list-of-number']),
    const=empty_list),
'vector-effect': SVGAttribute('vector-effect', anim=True,
    types=empty_list,
    const=frozenset([u'none', u'non-scaling-stroke', u'inherit'])),
'version': SVGAttribute('version', anim=False,
    types=empty_list,
    const=frozenset([u'1.1', u'1.2'])),
'viewBox': SVGAttribute('viewBox', anim=True,
    types=frozenset([u'list-of-numbers']),
    const=empty_list),
'viewport-fill': SVGAttribute('viewport-fill', anim=True,
    types=frozenset([u'color']),
    const=frozenset([u'none', u'inherit'])),
'viewport-fill-opacity': SVGAttribute('viewport-fill-opacity', anim=True,
    types=frozenset([u'number']),
    const=frozenset([u'inherit'])),
'visibility': SVGAttribute('visibility', anim=True,
    types=empty_list,
    const=frozenset([u'visible', u'hidden', u'inherit'])),
'width': SVGMultiAttribute({
    '*': SVGAttribute(
        'width', anim=True,
        types=frozenset([u'length']),
        const=empty_list),
    'textArea': SVGAttribute(
        'width', anim=True,
        types=frozenset([u'length']),
        const=frozenset([u'auto'])),
    }),
'widths': SVGAttribute('widths', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'x': SVGMultiAttribute({
    '*': SVGAttribute(
        'x', anim=True,
        types=frozenset([u'coordinate']),
        const=empty_list),
    'text': SVGAttribute(
        'x', anim=True,
        types=frozenset([u'list-of-coordinate']),
        const=empty_list),
    }),
'x-height': SVGAttribute('x-height', anim=False,
    types=frozenset([u'number']),
    const=empty_list),
'x1': SVGAttribute('x1', anim=True,
    types=frozenset([u'coordinate']),
    const=empty_list),
'x2': SVGAttribute('x2', anim=True,
    types=frozenset([u'coordinate']),
    const=empty_list),
'xlink:actuate': SVGMultiAttribute({
    '*': SVGAttribute(
        'xlink:actuate', anim=False,
        types=empty_list,
        const=frozenset([u'onLoad'])),
    'a': SVGAttribute(
        'xlink:actuate', anim=False,
        types=empty_list,
        const=frozenset([u'onRequest'])),
    }),
'xlink:arcrole': SVGAttribute('xlink:arcrole', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'xlink:href': SVGAttribute('xlink:href', anim=True,
    types=frozenset([u'IRI']),
    const=empty_list),
'xlink:role': SVGAttribute('xlink:role', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'xlink:show': SVGMultiAttribute({
    '*': SVGAttribute(
        'xlink:show', anim=False,
        types=empty_list,
        const=frozenset([u'other'])),
    'animation audio foreignObject image use video': SVGAttribute(
        'xlink:show', anim=False,
        types=empty_list,
        const=frozenset([u'embed'])),
    'a': SVGAttribute(
        'xlink:show', anim=False,
        types=empty_list,
        const=frozenset([u'new', u'replace'])),
    }),
'xlink:title': SVGAttribute('xlink:title', anim=False,
    types=frozenset([u'string']),
    const=empty_list),
'xlink:type': SVGAttribute('xlink:type', anim=True,
    types=empty_list,
    const=frozenset([u'simple'])),
'xmlns': SVGAttribute('xmlns', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'xmlns:xlink': SVGAttribute('xmlns:xlink', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'xmlns:ev': SVGAttribute('xmlns:ev', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'xml:base': SVGAttribute('xml:base', anim=False,
    types=frozenset([u'IRI']),
    const=empty_list),
'xml:id': SVGAttribute('xml:id', anim=False,
    types=frozenset([u'name']),
    const=empty_list),
'xml:lang': SVGAttribute('xml:lang', anim=False,
    types=frozenset([u'name']),
    const=empty_list),
'xml:space': SVGMultiAttribute({
    '*': SVGAttribute(
        'xml:space', anim=False,
        types=empty_list,
        const=frozenset([u'preserve', u'default'])),
    'handler script': SVGAttribute(
        'xml:space', anim=False,
        types=empty_list,
        const=frozenset([u'preserve'])),
    }),
'y': SVGMultiAttribute({
    '*': SVGAttribute(
        'y', anim=True,
        types=frozenset([u'coordinate']),
        const=empty_list),
    'text': SVGAttribute(
        'y', anim=True,
        types=frozenset([u'list-of-coordinate']),
        const=empty_list),
    }),
'y1': SVGAttribute('y1', anim=True,
    types=frozenset([u'coordinate']),
    const=empty_list),
'y2': SVGAttribute('y2', anim=True,
    types=frozenset([u'coordinate']),
    const=empty_list),
'zoomAndPan': SVGAttribute('zoomAndPan', anim=False,
    types=empty_list,
    const=frozenset([u'disable', u'magnify'])),
}

attribute_names = [u'slope', u'keySplines', u'rx', u'accumulate', u'bandwidth', u'attributeType', u'unicode', u'nav-right', u'arabic-form', u'y2', u'horiz-origin-x', u'underline-position', u'zoomAndPan', u'cap-height', u'defaultAction', u'to', u'syncBehavior', u'alphabetic', u'g2', u'g1', u'panose-1', u'strikethrough-thickness', u'attributeName', u'bbox', u'nav-up-left', u'nav-left', u'restart', u'target', u'xlink:actuate', u'rotate', u'resource', u'd', u'syncToleranceDefault', u'initialVisibility', u'transformBehavior', u'nav-up-right', u'keyTimes', u'x', u'requiredFormats', u'nav-next', u'glyph-name', u'xml:lang', u'mathematical', u'observer', u'repeatDur', u'hanging', u'y1', u'xml:base', u'ascent', u'event', u'strikethrough-position', u'overlay', u'rev', u'ry', u'overline-thickness', u'content', u'version', u'rel', u'focusable', u'requiredFonts', u'nav-down-right', u'xml:id', u'offset', u'additive', u'underline-thickness', u'font-family', u'by', u'mediaTime', u'timelineBegin', u'about', u'horiz-adv-x', u'widths', u'k', u'requiredFeatures', u'preserveAspectRatio', u'contentScriptType', u'origin', u'xml:space', u'xlink:href', u'height', u'baseProfile', u'cy', u'cx', u'path', u'xlink:role', u'from', u'u1', u'transform', u'units-per-em', u'u2', u'width', u'handler', u'font-variant', u'x-height', u'dur', u'xlink:arcrole', u'type', u'focusHighlight', u'mediaCharacterEncoding', u'xlink:title', u'editable', u'stemv', u'systemLanguage', u'x2', u'x1', u'ideographic', u'xlink:show', u'overline-position', u'syncTolerance', u'gradientUnits', u'r', u'values', u'typeof', u'mediaContentEncodings', u'property', u'requiredExtensions', u'repeatCount', u'ev:event', u'nav-down', u'mediaSize', u'pathLength', u'syncMaster', u'font-style', u'fill', u'end', u'descent', u'calcMode', u'min', u'stemh', u'id', u'unicode-range', u'nav-up', u'font-stretch', u'role', u'font-weight', u'begin', u'xlink:type', u'syncBehaviorDefault', u'max', u'snapshotTime', u'playbackOrder', u'keyPoints', u'nav-prev', u'propagate', u'phase', u'externalResourcesRequired', u'nav-down-left', u'class', u'lang', u'datatype', u'viewBox', u'points', u'accent-height', u'y']
property_names = [u'stroke-linejoin', u'font-size', u'text-rendering', u'color-rendering', u'fill-opacity', u'color', u'shape-rendering', u'solid-color', u'stroke', u'stroke-linecap', u'vector-effect', u'stroke-width', u'font-style', u'fill', u'solid-opacity', u'fill-rule', u'viewport-fill-opacity', u'display-align', u'buffered-rendering', u'stroke-miterlimit', u'font-variant', u'stop-opacity', u'font-weight', u'opacity', u'direction', u'audio-level', u'visibility', u'unicode-bidi', u'line-increment', u'image-rendering', u'font-family', u'viewport-fill', u'text-align', u'stroke-opacity', u'stroke-dashoffset', u'text-anchor', u'stop-color', u'pointer-events', u'stroke-dasharray', u'display']
media_group_names = ['audio-level', 'buffered-rendering', 'display', 'image-rendering', 'pointer-events', 'shape-rendering', 'text-rendering', 'viewport-fill', 'viewport-fill-opacity', 'visibility']
