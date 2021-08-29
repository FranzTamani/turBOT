#===================================
.intel_syntax noprefix
#===================================

nop
nop
nop
nop
nop
nop
nop
nop

#===================================
.section .interp ,"a",@progbits
#===================================

.align 1
          .byte 0x2f
          .byte 0x6c
          .byte 0x69
          .byte 0x62
          .byte 0x36
          .byte 0x34
          .byte 0x2f
          .byte 0x6c
          .byte 0x64
          .byte 0x2d
          .byte 0x6c
          .byte 0x69
          .byte 0x6e
          .byte 0x75
          .byte 0x78
          .byte 0x2d
          .byte 0x78
          .byte 0x38
          .byte 0x36
          .byte 0x2d
          .byte 0x36
          .byte 0x34
          .byte 0x2e
          .byte 0x73
          .byte 0x6f
          .byte 0x2e
          .byte 0x32
          .byte 0x0
#===================================
# end section .interp
#===================================

#===================================
.text
#===================================

          .byte 0xf
          .byte 0x1f
          .byte 0x80
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0xf
          .byte 0x1f
          .byte 0x80
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0x66
          .byte 0xf
          .byte 0x1f
          .byte 0x44
          .byte 0x0
          .byte 0x0
          .byte 0xf
          .byte 0x1f
          .byte 0x80
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0xf
          .byte 0x1f
          .byte 0x0
          .byte 0xf
          .byte 0x1f
          .byte 0x80
          .byte 0x0
          .byte 0x0
          .byte 0x0
          .byte 0x0
#-----------------------------------
.globl main
.type main, @function
#-----------------------------------
main:

.cfi_startproc 
.cfi_lsda 255
.cfi_personality 255
.cfi_def_cfa 7, 8
.cfi_offset 16, -8
            nop
            nop
            nop
            nop
            push RBP
.cfi_def_cfa_offset 16
.cfi_offset 6, -16
            mov RBP,RSP
.cfi_def_cfa_register 6
            mov EAX,0
            pop RBP
.cfi_def_cfa 7, 8
            ret 
.cfi_endproc 

            nop
            nop
            nop
            nop
            nop
            nop
            nop
            nop
#===================================
# end section .text
#===================================

#===================================
.section .rodata ,"a",@progbits
#===================================

.align 4
          .byte 0x1
          .byte 0x0
          .byte 0x2
          .byte 0x0
#===================================
# end section .rodata
#===================================

#===================================
.section .init_array ,"wa"
#===================================

.align 8
__frame_dummy_init_array_entry:
__init_array_start:
#===================================
# end section .init_array
#===================================

#===================================
.section .fini_array ,"wa"
#===================================

.align 8
__do_global_dtors_aux_fini_array_entry:
__init_array_end:
#===================================
# end section .fini_array
#===================================

#===================================
.data
#===================================

.align 8
#-----------------------------------
.weak data_start
.type data_start, @notype
#-----------------------------------
data_start:
          .zero 8
          .quad 0
#           : WARNING:0: no symbol for address 0x4008 
#===================================
# end section .data
#===================================

#===================================
.bss
#===================================

.align 1
completed.8060:
#-----------------------------------
.globl _edata
.type _edata, @notype
#-----------------------------------
_edata:
          .zero 8
#-----------------------------------
.globl _end
.type _end, @notype
#-----------------------------------
_end:
#===================================
# end section .bss
#===================================
#-----------------------------------
.globl __libc_start_main
.type __libc_start_main, @function
#-----------------------------------
#-----------------------------------
.weak __cxa_finalize
.type __cxa_finalize, @function
#-----------------------------------
#-----------------------------------
.weak _ITM_deregisterTMCloneTable
.type _ITM_deregisterTMCloneTable, @notype
#-----------------------------------
#-----------------------------------
.weak _ITM_registerTMCloneTable
.type _ITM_registerTMCloneTable, @notype
#-----------------------------------
#-----------------------------------
.weak __gmon_start__
.type __gmon_start__, @notype
#-----------------------------------
