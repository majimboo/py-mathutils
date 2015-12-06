#include "MEM_guardedalloc.h"
#include "BLI_memarena.h"

#include <assert.h>

void *MEM_mallocN(size_t len, const char * str) { assert(0); return (void *)0; };
void *MEM_callocN(size_t len, const char * str) { assert(0); return (void *)0; };
short MEM_freeN(void *vmemh) { return 0; }

void *BLI_memarena_alloc(struct MemArena *ma, int size) { assert(0); return (void *)0; }

#ifndef NDEBUG
void BLI_system_backtrace(FILE *fp) { };
#endif
