// generated by go generate; DO NOT EDIT.

package main

// This data is derived from files in the font/fixed directory of the Plan 9
// Port source code (https://github.com/9fans/plan9port) which were originally
// based on the public domain X11 misc-fixed font files.

import (
	"image"
	"image/color"
	"image/draw"

	"periph.io/x/periph/devices/ssd1306/image1bit"
)

type bit bool

func (b bit) RGBA() (uint32, uint32, uint32, uint32) {
	if b {
		return 65535, 65535, 65535, 65535
	}
	return 0, 0, 0, 0
}

func convertBit(c color.Color) color.Color {
	r, g, b, _ := c.RGBA()
	return bit((r | g | b) >= 0x8000)
}

type alpha struct {
	image1bit.VerticalLSB
}

func (a *alpha) ColorModel() color.Model {
	return color.ModelFunc(convertBit)
}

func (a *alpha) At(x, y int) color.Color {
	return convertBit(a.VerticalLSB.At(x, y))
}

// glyphs contains chars 0x21 to 0x7F.
var glyphs = []alpha{
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 248, 0, 0, 0, 0, 0, 11, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 56, 0, 56, 0, 0, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 64, 240, 64, 240, 64, 0, 1, 7, 1, 7, 1},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 64, 160, 240, 160, 32, 0, 2, 2, 7, 2, 1},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{16, 40, 16, 192, 32, 24, 12, 2, 1, 4, 10, 4},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{192, 32, 32, 192, 0, 0, 6, 9, 9, 10, 4, 10},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 56, 0, 0, 0, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 192, 48, 8, 0, 0, 0, 1, 6, 8, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 8, 48, 192, 0, 0, 0, 8, 6, 1, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 160, 192, 192, 160, 128, 0, 2, 1, 1, 2, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 128, 128, 224, 128, 128, 0, 0, 0, 3, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 0, 0, 0, 0, 16, 12, 12, 4, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 128, 128, 128, 128, 128, 0, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 0, 0, 0, 0, 0, 8, 28, 8, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 128, 96, 24, 0, 12, 3, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{224, 16, 8, 8, 16, 224, 3, 4, 8, 8, 4, 3},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 32, 16, 248, 0, 0, 0, 8, 8, 15, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{48, 8, 8, 8, 136, 112, 12, 10, 9, 9, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{8, 8, 136, 200, 168, 24, 4, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 32, 16, 248, 0, 3, 2, 2, 2, 15, 2},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 136, 72, 72, 72, 136, 4, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{224, 16, 136, 136, 136, 0, 7, 9, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{8, 8, 8, 200, 40, 24, 0, 12, 3, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{112, 136, 136, 136, 136, 112, 7, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{112, 136, 136, 136, 72, 240, 0, 8, 8, 8, 4, 3},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 64, 224, 64, 0, 0, 0, 8, 28, 8, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 64, 224, 64, 0, 0, 16, 12, 12, 4, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 128, 64, 32, 16, 8, 0, 0, 1, 2, 4, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{64, 64, 64, 64, 64, 64, 2, 2, 2, 2, 2, 2},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 8, 16, 32, 64, 128, 0, 8, 4, 2, 1, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{48, 8, 8, 8, 136, 112, 0, 0, 0, 11, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{240, 8, 136, 72, 72, 240, 7, 8, 9, 10, 9, 3},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{224, 16, 8, 8, 16, 224, 15, 1, 1, 1, 1, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{8, 248, 136, 136, 136, 112, 8, 15, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{240, 8, 8, 8, 8, 16, 7, 8, 8, 8, 8, 4},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{8, 248, 8, 8, 8, 240, 8, 15, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 136, 136, 136, 8, 8, 15, 8, 8, 8, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 136, 136, 136, 8, 8, 15, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{240, 8, 8, 8, 8, 16, 7, 8, 8, 9, 5, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 128, 128, 128, 128, 248, 15, 0, 0, 0, 0, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 8, 8, 248, 8, 8, 0, 8, 8, 15, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 8, 248, 8, 4, 8, 8, 8, 7, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 128, 64, 32, 16, 8, 15, 0, 1, 2, 4, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 0, 0, 0, 0, 0, 15, 8, 8, 8, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 48, 192, 192, 48, 248, 15, 0, 0, 0, 0, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 32, 64, 128, 0, 248, 15, 0, 0, 0, 1, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{240, 8, 8, 8, 8, 240, 7, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 136, 136, 136, 136, 112, 15, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{240, 8, 8, 8, 8, 240, 7, 8, 10, 12, 8, 23},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 136, 136, 136, 136, 112, 15, 0, 1, 2, 4, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{112, 136, 136, 136, 136, 16, 4, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 8, 8, 248, 8, 8, 0, 0, 0, 15, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 0, 0, 0, 0, 248, 7, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{56, 192, 0, 0, 192, 56, 0, 1, 14, 14, 1, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 0, 128, 128, 0, 248, 15, 6, 1, 1, 6, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{24, 96, 128, 128, 96, 24, 12, 3, 0, 0, 3, 12},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 24, 96, 128, 96, 24, 0, 0, 0, 15, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{8, 8, 136, 200, 40, 24, 12, 10, 9, 8, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 252, 4, 4, 4, 0, 0, 31, 16, 16, 16, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 24, 96, 128, 0, 0, 0, 0, 0, 0, 3, 12},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 4, 4, 4, 252, 0, 0, 16, 16, 16, 31, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 32, 16, 8, 16, 32, 0, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 16},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 4, 8, 0, 0, 0, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 64, 64, 64, 64, 128, 6, 9, 9, 9, 5, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 128, 64, 64, 64, 128, 15, 4, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 64, 128, 7, 8, 8, 8, 8, 4},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 128, 248, 7, 8, 8, 8, 4, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 64, 128, 7, 9, 9, 9, 9, 5},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 240, 136, 136, 8, 16, 0, 15, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 128, 64, 21, 10, 10, 10, 9, 16},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 128, 64, 64, 64, 128, 15, 0, 0, 0, 0, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 64, 208, 0, 0, 0, 8, 8, 15, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 0, 64, 208, 0, 24, 0, 0, 0, 31},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{248, 0, 0, 128, 64, 0, 15, 1, 1, 2, 4, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 8, 248, 0, 0, 0, 8, 8, 15, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 192, 64, 128, 64, 128, 0, 15, 0, 7, 0, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{192, 128, 64, 64, 64, 128, 15, 0, 0, 0, 0, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 64, 128, 7, 8, 8, 8, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{192, 128, 64, 64, 64, 128, 31, 2, 4, 4, 4, 3},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 128, 192, 3, 4, 4, 4, 2, 31},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{64, 128, 64, 64, 64, 128, 0, 15, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{128, 64, 64, 64, 64, 128, 4, 9, 9, 10, 10, 4},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{64, 240, 64, 64, 0, 0, 0, 7, 8, 8, 8, 4},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{192, 0, 0, 0, 0, 192, 7, 8, 8, 8, 4, 15},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 192, 0, 0, 0, 192, 0, 1, 6, 8, 6, 1},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 192, 0, 0, 0, 192, 0, 7, 8, 7, 8, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{64, 128, 0, 0, 128, 64, 8, 4, 3, 3, 4, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{192, 0, 0, 0, 0, 192, 19, 4, 4, 4, 2, 31},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{64, 64, 64, 64, 192, 64, 8, 12, 10, 9, 8, 8},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 128, 184, 68, 4, 4, 0, 0, 14, 17, 16, 16},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 0, 0, 248, 0, 0, 0, 0, 0, 15, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 4, 4, 68, 184, 128, 0, 16, 16, 17, 14, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 48, 8, 16, 32, 24, 0, 0, 0, 0, 0, 0},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
	{
		image1bit.VerticalLSB{
			Pix:    []byte{0, 240, 216, 104, 152, 240, 0, 7, 15, 10, 15, 7},
			Stride: 6,
			Rect:   image.Rectangle{Max: image.Point{6, 13}},
		},
	},
}

// drawText draws text on an image.
//
// It is intentionally very limited. Use golang.org/x/image/font for complete
// functionality.
func drawText(dst draw.Image, p image.Point, t string) {
	const base = 0x21
	r := image.Rect(0, 0, 7, 13).Add(p)
	u := image.Uniform{C: image1bit.On}
	for _, c := range t {
		if c >= base && int(c-base) < len(glyphs) {
			draw.DrawMask(dst, r, &u, image.Point{}, &glyphs[c-base], image.Point{}, draw.Over)
		}
		r = r.Add(image.Point{7, 0})
	}
}
