#include "MEM_guardedalloc.h"
#include "BLI_memarena.h"

void *MEM_callocN(size_t len, const char * str) { return (void *)0; };
short MEM_freeN(void *vmemh) { return 0; }

void *BLI_memarena_alloc(struct MemArena *ma, int size) { return (void *)0; }
